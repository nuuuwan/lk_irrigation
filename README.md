# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_07:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,169 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 07:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | -0.062 |  |
| 2026-09-27 07:14:32 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:14:16 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.067 |  |
| 2026-09-27 07:12:19 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 07:11:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:10:47 | Glencourse (Kelani Ganga) | 12.18 | 🟢 Normal | -0.043 |  |
| 2026-09-27 07:10:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:10:03 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.181 |  |
| 2026-09-27 07:09:29 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-27 07:09:29 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:08:47 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.066 |  |
| 2026-09-27 07:07:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:07:25 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:06:51 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:05:50 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:04:50 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | -0.049 |  |
| 2026-09-27 07:04:42 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:04:16 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:04:12 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-09-27 07:04:02 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.074 |  |
| 2026-09-27 07:03:44 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.019 |  |
| 2026-09-27 07:03:35 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.029 |  |
| 2026-09-27 07:03:17 | Rathnapura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.068 |  |
| 2026-09-27 07:03:12 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:03:07 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:02:56 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-09-27 07:02:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.166 |  |
| 2026-09-27 07:02:37 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-09-27 07:02:26 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.072 |  |
| 2026-09-27 07:02:18 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-09-27 07:02:15 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.039 |  |
| 2026-09-27 07:02:09 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:01:44 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.031 |  |
| 2026-09-27 07:01:36 | Panadugama (Nilwala Ganga) | 5.48 | 🟡 Alert | -0.052 |  |
| 2026-09-27 07:01:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-09-27 07:01:10 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.123 |  |
| 2026-09-27 07:00:50 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:00:37 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:00:34 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 07:12:19 | Baddegama (Gin Ganga) | 4.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 07:00:34 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 07:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | -0.062 |  |
| 2026-09-27 07:01:36 | Panadugama (Nilwala Ganga) | 5.48 | 🟡 Alert | -0.052 |  |
| 2026-09-27 07:00:37 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:11:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:00:50 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:07:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:14:32 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:10:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:02:37 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:04:42 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:03:12 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:03:07 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 07:09:29 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-27 07:05:50 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:06:51 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:04:16 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:02:09 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-27 07:03:44 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | -0.019 |  |
| 2026-09-27 07:01:12 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-09-27 07:02:56 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-09-27 07:04:12 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-09-27 07:03:35 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.029 |  |
| 2026-09-27 07:02:18 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-09-27 07:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.030 |  |
| 2026-09-27 07:01:44 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.031 |  |
| 2026-09-27 07:02:15 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.039 |  |
| 2026-09-27 07:10:47 | Glencourse (Kelani Ganga) | 12.18 | 🟢 Normal | -0.043 |  |
| 2026-09-27 07:04:50 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | -0.049 |  |
| 2026-09-27 07:08:47 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.066 |  |
| 2026-09-27 07:14:16 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | -0.067 |  |
| 2026-09-27 07:03:17 | Rathnapura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.068 |  |
| 2026-09-27 07:02:26 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.072 |  |
| 2026-09-27 07:04:02 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.074 |  |
| 2026-09-27 07:01:10 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.123 |  |
| 2026-09-27 07:02:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.166 |  |
| 2026-09-27 07:10:03 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)