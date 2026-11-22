# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_15:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,790 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 15:03:20 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-11-22 15:03:19 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-22 15:03:10 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.089 |  |
| 2026-11-22 15:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:02:36 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.060 |  |
| 2026-11-22 15:02:34 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-11-22 15:02:33 | Moragaswewa (Deduru Oya) | 3.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 15:02:31 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.020 |  |
| 2026-11-22 15:02:23 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 15:02:20 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 15:01:31 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-11-22 15:01:26 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:24 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:19 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 15:01:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:07 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-22 15:00:48 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:00:45 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.012 |  |
| 2026-11-22 15:00:24 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:00:18 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:00:10 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.083 |  |
| 2026-11-22 14:29:50 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 15:02:33 | Moragaswewa (Deduru Oya) | 3.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 15:01:19 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 14:01:39 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 15:02:20 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 15:02:23 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 15:00:48 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:00:24 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:13:48 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:03:10 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:16:01 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:02:40 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:10:24 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:06:06 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:03:08 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:26 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-22 14:16:26 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:01:24 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-22 15:03:19 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-22 15:03:20 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-11-22 15:01:31 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-11-22 14:00:53 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-11-22 15:00:45 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.012 |  |
| 2026-11-22 15:02:34 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-11-22 15:01:07 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-22 15:02:31 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.020 |  |
| 2026-11-22 14:12:00 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.035 |  |
| 2026-11-22 14:08:02 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.040 |  |
| 2026-11-22 14:04:23 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.041 |  |
| 2026-11-22 15:02:36 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.060 |  |
| 2026-11-22 14:08:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.067 |  |
| 2026-11-22 14:06:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.071 |  |
| 2026-11-22 14:04:14 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.076 |  |
| 2026-11-22 15:00:10 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.083 |  |
| 2026-11-22 15:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.089 |  |
| 2026-11-22 14:02:39 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)