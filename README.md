# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_09:13:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,851 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 09:13:05 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:12:03 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-06-25 09:09:10 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-06-25 09:08:58 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.109 |  |
| 2026-06-25 09:08:01 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:08:00 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-25 09:06:37 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.084 |  |
| 2026-06-25 09:06:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:05:12 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-06-25 09:05:07 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:05:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-25 09:04:19 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-25 09:04:17 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-06-25 09:04:13 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.051 |  |
| 2026-06-25 09:03:28 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:03:15 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:03:10 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.069 |  |
| 2026-06-25 09:02:48 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-25 09:02:46 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:02:45 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.010 |  |
| 2026-06-25 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.55 | 🟢 Normal | -0.030 |  |
| 2026-06-25 09:02:29 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:02:23 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-25 09:02:11 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:02:06 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.021 |  |
| 2026-06-25 09:02:01 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 09:01:53 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 09:01:51 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-06-25 09:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:01:38 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 09:01:30 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:01:10 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:00:22 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:00:21 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-06-25 09:00:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.077 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 09:05:12 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-06-25 09:00:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-25 09:02:48 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-25 09:01:38 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 09:05:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-25 09:01:53 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 09:02:01 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 09:00:22 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:01:10 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:03:28 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:01:25 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:13:05 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:01:30 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:02:46 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:02:29 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-25 08:06:28 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:12:03 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:06:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:03:15 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:08:01 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:05:07 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:02:11 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 09:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-06-25 09:09:10 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-06-25 08:08:04 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.009 |  |
| 2026-06-25 09:04:19 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-25 09:02:45 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.010 |  |
| 2026-06-25 09:00:21 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-06-25 09:08:00 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-25 09:01:51 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-06-25 09:02:06 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.021 |  |
| 2026-06-25 09:04:17 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-06-25 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.55 | 🟢 Normal | -0.030 |  |
| 2026-06-25 09:02:23 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-25 09:04:13 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.051 |  |
| 2026-06-25 09:03:10 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.069 |  |
| 2026-06-25 09:06:37 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.084 |  |
| 2026-06-25 09:08:58 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)