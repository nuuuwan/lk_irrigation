# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_08:17:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 08:17:08 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-02-08 08:15:30 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-02-08 08:14:29 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:12:42 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.082 |  |
| 2026-02-08 08:12:01 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-02-08 08:09:16 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:08:35 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-02-08 08:07:38 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.006 |  |
| 2026-02-08 08:07:22 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:06:47 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 08:06:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-08 08:05:53 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.028 |  |
| 2026-02-08 08:05:45 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:04:14 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-08 08:04:12 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-08 08:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:03:41 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:03:35 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-02-08 08:03:28 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:03:12 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-08 08:02:44 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:41 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:34 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:33 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:27 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:02:04 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:01:59 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:01:53 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:01:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:01:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.098 |  |
| 2026-02-08 08:01:49 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.089 |  |
| 2026-02-08 08:01:24 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-02-08 08:01:21 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.014 |  |
| 2026-02-08 08:01:15 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:01:10 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:01:07 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:01:01 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-02-08 07:42:36 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 08:04:14 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-08 08:03:12 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-08 08:04:12 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-08 08:06:47 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 08:06:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-08 07:24:07 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-08 08:02:04 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:01:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:44 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:09:16 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:07:22 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:03:41 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:14:29 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:41 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:34 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:01:07 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:02:33 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:03:28 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:01:59 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:05:45 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-08 08:07:38 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.006 |  |
| 2026-02-08 08:17:08 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-02-08 08:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:02:27 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:01:01 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:01:15 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:01:53 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:01:10 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-02-08 08:03:35 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-02-08 08:01:21 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.014 |  |
| 2026-02-08 08:15:30 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-02-08 08:12:01 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-02-08 07:08:35 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-02-08 08:01:24 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-02-08 08:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.028 |  |
| 2026-02-08 08:08:35 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-02-08 08:12:42 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.082 |  |
| 2026-02-08 08:01:49 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.089 |  |
| 2026-02-08 08:01:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)