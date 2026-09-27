# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_08:15:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 08:15:03 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 08:11:16 | Magura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-09-27 08:10:37 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.017 |  |
| 2026-09-27 08:09:59 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:09:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.046 |  |
| 2026-09-27 08:07:53 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.036 |  |
| 2026-09-27 08:07:39 | Panadugama (Nilwala Ganga) | 5.44 | 🟡 Alert | -0.036 |  |
| 2026-09-27 08:07:19 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.048 |  |
| 2026-09-27 08:06:45 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:05:24 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:05:22 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.033 |  |
| 2026-09-27 08:04:40 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.059 |  |
| 2026-09-27 08:04:34 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:04:33 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:04:33 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-27 08:04:33 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:04:13 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-27 08:04:06 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | -0.060 |  |
| 2026-09-27 08:03:56 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:03:43 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.073 |  |
| 2026-09-27 08:03:34 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:03:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:03:26 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:03:23 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-09-27 08:03:20 | Rathnapura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.070 |  |
| 2026-09-27 08:03:15 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:03:00 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:02:53 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:02:03 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:01:35 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.041 |  |
| 2026-09-27 08:01:17 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:00:58 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:00:15 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:00:15 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:59:56 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 08:15:03 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 08:07:53 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.036 |  |
| 2026-09-27 08:09:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.046 |  |
| 2026-09-27 08:07:39 | Panadugama (Nilwala Ganga) | 5.44 | 🟡 Alert | -0.036 |  |
| 2026-09-27 08:04:13 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-27 08:04:33 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-27 08:03:34 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:00:15 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:11:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:02:03 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:04:33 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:03:26 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:03:00 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:10:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:03:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:00:15 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:06:45 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:04:34 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:01:35 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:05:24 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:01:17 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:00:58 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-27 08:09:59 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:03:56 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:03:15 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:02:53 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:04:33 | Putupaula (Kalu Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-09-27 08:10:37 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.017 |  |
| 2026-09-27 08:11:16 | Magura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-09-27 08:03:23 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-09-27 08:05:22 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.033 |  |
| 2026-09-27 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.041 |  |
| 2026-09-27 07:59:56 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.041 |  |
| 2026-09-27 08:07:19 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | -0.048 |  |
| 2026-09-27 08:04:40 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.059 |  |
| 2026-09-27 08:04:06 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | -0.060 |  |
| 2026-09-27 08:03:20 | Rathnapura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.070 |  |
| 2026-09-27 08:03:43 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)