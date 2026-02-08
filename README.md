# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_09:17:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,338 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 09:17:26 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.026 |  |
| 2026-02-08 09:13:19 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.109 |  |
| 2026-02-08 09:13:06 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:10:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -90.000 |  |
| 2026-02-08 09:10:39 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -90.000 |  |
| 2026-02-08 09:09:36 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-08 09:08:14 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:07:55 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:07:19 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:07:13 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-02-08 09:06:54 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:06:53 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-02-08 09:05:00 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:04:45 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.013 |  |
| 2026-02-08 09:04:41 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:04:15 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:03:48 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.118 |  |
| 2026-02-08 09:03:37 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:03:29 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 09:03:25 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:03:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:03:20 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-08 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-02-08 09:03:06 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-08 09:02:57 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-08 09:02:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:02:19 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:02:12 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:01:55 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:01:48 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-08 09:01:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.070 |  |
| 2026-02-08 09:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:01:11 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:01:08 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:00:55 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:47 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:31 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 09:01:48 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-08 09:03:06 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-08 09:03:20 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-08 09:03:29 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 09:09:36 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-08 09:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:31 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:02:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:06:54 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:07:19 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:13:06 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:55 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:04:15 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:08:14 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:07:55 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:02:19 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:00:47 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:02:12 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:03:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:04:41 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 09:06:53 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-02-08 09:05:00 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:03:25 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:01:55 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:01:08 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:01:11 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-08 09:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:03:35 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-02-08 09:02:57 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-08 09:07:13 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-02-08 09:04:45 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.013 |  |
| 2026-02-08 09:17:26 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.026 |  |
| 2026-02-08 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-02-08 09:00:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.062 |  |
| 2026-02-08 09:01:33 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.070 |  |
| 2026-02-08 09:13:19 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.109 |  |
| 2026-02-08 09:03:48 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.118 |  |
| 2026-02-08 09:10:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)