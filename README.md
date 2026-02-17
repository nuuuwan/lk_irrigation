# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_08:06:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 08:06:08 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:05:05 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.077 |  |
| 2026-02-17 08:04:52 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-17 08:04:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.377 |  |
| 2026-02-17 08:04:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:04:10 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.071 |  |
| 2026-02-17 08:03:55 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:03:49 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 08:03:43 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.302 |  |
| 2026-02-17 08:03:14 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:03:07 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-17 08:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-02-17 08:02:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:02:31 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.021 |  |
| 2026-02-17 08:02:28 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.084 |  |
| 2026-02-17 08:02:21 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:02:19 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:02:14 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:02:11 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:02:04 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:58 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:35 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:34 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:24 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 1.037 | 🔺 Rising |
| 2026-02-17 08:01:18 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:00:49 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-17 08:00:43 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:00:37 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-02-17 08:00:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:33:58 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.077 |  |
| 2026-02-17 07:26:26 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:22:39 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -3.312 |  |
| 2026-02-17 07:16:31 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-02-17 07:13:02 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:12:05 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-17 07:11:34 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:11:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-02-17 07:11:09 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 08:01:24 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 1.037 | 🔺 Rising |
| 2026-02-17 07:11:09 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-17 08:03:49 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 08:00:49 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-17 08:01:58 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:00:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:11:34 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:01:54 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:02:19 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:13:02 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:03:14 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:02:11 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:35 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:18 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:00:43 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:02:04 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:01:34 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:08:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:04:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 08:02:21 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-17 07:11:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-02-17 07:16:31 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-02-17 08:02:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:03:55 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:02:14 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:06:08 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-17 08:03:07 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-17 08:00:37 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-02-17 08:04:52 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-17 08:02:31 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.021 |  |
| 2026-02-17 08:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-02-17 08:04:10 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.071 |  |
| 2026-02-17 08:05:05 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.077 |  |
| 2026-02-17 08:02:28 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.084 |  |
| 2026-02-17 08:03:43 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.302 |  |
| 2026-02-17 08:04:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.377 |  |
| 2026-02-17 07:22:39 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -3.312 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)