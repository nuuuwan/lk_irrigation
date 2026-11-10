# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_09:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,846 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 09:03:20 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.188 |  |
| 2026-11-10 09:03:16 | Giriulla (Maha Oya) | 2.74 | 🟢 Normal | -0.102 |  |
| 2026-11-10 09:03:09 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-10 09:03:01 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.043 |  |
| 2026-11-10 09:03:00 | Moraketiya (Walawe Ganga) | 3.02 | 🟡 Alert | -0.031 |  |
| 2026-11-10 09:02:54 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:02:36 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.960 | 🔺 Rising |
| 2026-11-10 09:02:28 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-10 09:02:23 | Panadugama (Nilwala Ganga) | 6.07 | 🟠 Minor Flood | -0.030 |  |
| 2026-11-10 09:02:13 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-10 09:02:06 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-10 09:02:03 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 09:02:01 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-11-10 09:02:01 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.040 |  |
| 2026-11-10 09:01:52 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-11-10 09:01:23 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.108 |  |
| 2026-11-10 09:01:18 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.079 |  |
| 2026-11-10 09:00:48 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 08:08:33 | Baddegama (Gin Ganga) | 4.16 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-11-10 09:02:03 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 09:02:23 | Panadugama (Nilwala Ganga) | 6.07 | 🟠 Minor Flood | -0.030 |  |
| 2026-11-10 08:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-10 09:02:13 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-10 09:03:00 | Moraketiya (Walawe Ganga) | 3.02 | 🟡 Alert | -0.031 |  |
| 2026-11-10 08:10:48 | Magura (Kalu Ganga) | 5.09 | 🟡 Alert | -0.049 |  |
| 2026-11-10 08:08:41 | Thawalama (Gin Ganga) | 4.49 | 🟡 Alert | -0.137 |  |
| 2026-11-10 09:02:36 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | 0.960 | 🔺 Rising |
| 2026-11-10 09:02:06 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-10 08:06:17 | Moragaswewa (Deduru Oya) | 4.11 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-10 08:09:04 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-10 08:00:13 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 09:02:54 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:01:52 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-10 08:07:04 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:00:48 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-10 09:03:09 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-10 09:02:28 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-10 09:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-11-10 09:02:01 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.029 |  |
| 2026-11-10 08:02:37 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-11-10 08:05:44 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | -0.032 |  |
| 2026-11-10 09:02:01 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.040 |  |
| 2026-11-10 08:14:22 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.041 |  |
| 2026-11-10 09:03:01 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.043 |  |
| 2026-11-10 08:04:34 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.052 |  |
| 2026-11-10 08:07:21 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | -0.057 |  |
| 2026-11-10 08:03:16 | Hanwella (Kelani Ganga) | 6.17 | 🟢 Normal | -0.063 |  |
| 2026-11-10 08:01:26 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2026-11-10 08:06:00 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | -0.066 |  |
| 2026-11-10 09:01:18 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.079 |  |
| 2026-11-10 08:01:52 | Rathnapura (Kalu Ganga) | 4.98 | 🟢 Normal | -0.093 |  |
| 2026-11-10 09:03:16 | Giriulla (Maha Oya) | 2.74 | 🟢 Normal | -0.102 |  |
| 2026-11-10 09:01:23 | Peradeniya (Mahaweli Ganga) | 3.55 | 🟢 Normal | -0.108 |  |
| 2026-11-10 08:09:53 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | -0.144 |  |
| 2026-11-10 09:03:20 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.188 |  |
| 2026-11-10 08:10:08 | Glencourse (Kelani Ganga) | 13.56 | 🟢 Normal | -0.278 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)