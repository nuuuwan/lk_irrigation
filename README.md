# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_15:03:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,075 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 15:03:29 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:03:27 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-11-10 15:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-10 15:03:13 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.188 |  |
| 2026-11-10 15:03:02 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.078 |  |
| 2026-11-10 15:03:01 | Dunamale (Aththanagalu Oya) | 4.56 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-10 15:03:00 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | -0.031 |  |
| 2026-11-10 15:03:00 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-10 15:02:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:02:53 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:02:23 | Rathnapura (Kalu Ganga) | 4.37 | 🟢 Normal | -0.043 |  |
| 2026-11-10 15:02:23 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | -0.040 |  |
| 2026-11-10 15:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-10 15:02:16 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-11-10 15:02:08 | Moraketiya (Walawe Ganga) | 3.00 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-11-10 15:01:39 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-11-10 15:01:39 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-10 15:01:33 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.052 |  |
| 2026-11-10 15:01:16 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-11-10 15:01:07 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:01:06 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.053 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 15:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-10 14:07:20 | Baddegama (Gin Ganga) | 4.24 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-11-10 15:03:01 | Dunamale (Aththanagalu Oya) | 4.56 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-10 15:02:08 | Moraketiya (Walawe Ganga) | 3.00 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-11-10 14:03:16 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 15:03:00 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | -0.031 |  |
| 2026-11-10 14:10:41 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.049 |  |
| 2026-11-10 15:01:39 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-10 15:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-10 15:03:00 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-10 15:01:06 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-10 14:04:10 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 14:02:13 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-10 15:02:53 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:15:01 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:04:04 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46⌛ | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:01:57 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:02:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:03:29 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:01:07 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:01:38 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-10 15:02:16 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-11-10 15:01:39 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-11-10 15:03:27 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-11-10 14:07:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-11-10 15:01:16 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-11-10 14:04:40 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.032 |  |
| 2026-11-10 15:02:23 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | -0.040 |  |
| 2026-11-10 15:02:23 | Rathnapura (Kalu Ganga) | 4.37 | 🟢 Normal | -0.043 |  |
| 2026-11-10 15:01:33 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.052 |  |
| 2026-11-10 14:08:45 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | -0.057 |  |
| 2026-11-10 15:03:02 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.078 |  |
| 2026-11-10 14:02:10 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.093 |  |
| 2026-11-10 14:09:33 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.141 |  |
| 2026-11-10 14:02:58 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.171 |  |
| 2026-11-10 15:03:13 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.188 |  |
| 2026-11-10 14:03:20 | Glencourse (Kelani Ganga) | 12.16 | 🟢 Normal | -0.194 |  |
| 2026-11-10 14:04:42 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)