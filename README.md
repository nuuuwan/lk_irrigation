# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_09:10:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 09:10:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:09:07 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:08:50 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-04 09:08:50 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-10-04 09:08:35 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:07:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-04 09:07:01 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:05:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:05:50 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.040 |  |
| 2026-10-04 09:04:53 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:04:28 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.060 |  |
| 2026-10-04 09:04:22 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 09:04:16 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:04:12 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:03:39 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:03:38 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-04 09:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 09:03:10 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-10-04 09:03:00 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-10-04 09:02:56 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:02:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:02:40 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:02:40 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.125 |  |
| 2026-10-04 09:02:40 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-10-04 09:02:24 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-04 09:02:06 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 09:01:58 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.070 |  |
| 2026-10-04 09:01:41 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-04 09:01:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:01:08 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:01:02 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 09:00:52 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-10-04 09:00:45 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:00:29 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:00:28 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:00:11 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 09:07:52 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-04 09:08:50 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-04 09:02:24 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-04 09:04:22 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 09:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-04 09:01:02 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 09:02:06 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 09:00:29 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:01:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:01:08 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:04:53 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:08:35 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:09:07 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:10:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:05:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:04:12 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:07:01 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:00:45 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:02:40 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:00:28 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:04:16 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:03:39 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 09:08:50 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-10-04 09:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-04 09:03:38 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-10-04 09:02:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:02:56 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:01:41 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-04 09:03:10 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-10-04 09:00:52 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-10-04 09:03:00 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-10-04 09:05:50 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.040 |  |
| 2026-10-04 09:00:11 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.050 |  |
| 2026-10-04 09:02:40 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.051 |  |
| 2026-10-04 09:04:28 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.060 |  |
| 2026-10-04 09:01:58 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.070 |  |
| 2026-10-04 09:02:40 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.125 |  |
| 2026-10-04 08:02:33 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)