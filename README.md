# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_15:02:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,973 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 15:02:58 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 15:02:49 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:48 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-11-11 15:02:41 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.078 |  |
| 2026-11-11 15:02:39 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:15 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 15:02:05 | Moragaswewa (Deduru Oya) | 3.22 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-11 15:01:58 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:01:29 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-11-11 15:01:26 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:00:50 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-11 15:00:26 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.210 |  |
| 2026-11-11 15:00:14 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-11-11 14:30:56 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-11 14:27:58 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 14:02:06 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 14:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-11 14:06:09 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-11 14:03:19 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | -0.049 |  |
| 2026-11-11 14:15:05 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | -0.062 |  |
| 2026-11-11 15:02:05 | Moragaswewa (Deduru Oya) | 3.22 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-11 14:00:39 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-11 14:30:56 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-11 14:03:23 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 14:04:01 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-11 15:02:15 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 14:08:34 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-11 15:02:58 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 14:02:39 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:01:58 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:49 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:01:26 | Ellagawa (Kalu Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:01:51 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 15:02:39 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-11 14:08:59 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.009 |  |
| 2026-11-11 14:03:55 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-11 15:00:50 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-11 14:06:40 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-11 14:02:06 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 15:02:48 | Pitabeddara (Nilwala Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-11-11 14:04:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-11-11 15:01:29 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-11-11 15:00:14 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-11-11 14:04:37 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.029 |  |
| 2026-11-11 14:02:26 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-11-11 14:02:17 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.043 |  |
| 2026-11-11 14:13:09 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.074 |  |
| 2026-11-11 15:02:41 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.078 |  |
| 2026-11-11 14:00:15 | Rathnapura (Kalu Ganga) | 4.03 | 🟢 Normal | -0.087 |  |
| 2026-11-11 14:03:30 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | -0.093 |  |
| 2026-11-11 14:05:23 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.107 |  |
| 2026-11-11 14:07:19 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.116 |  |
| 2026-11-11 15:00:26 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)