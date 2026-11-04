# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_01:03:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,073 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 01:03:51 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-05 01:03:40 | Giriulla (Maha Oya) | 3.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-05 01:03:37 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.088 |  |
| 2026-11-05 01:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-05 01:03:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:03:33 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-05 01:03:26 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-05 01:03:19 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.021 |  |
| 2026-11-05 01:02:18 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-05 01:02:03 | Moragaswewa (Deduru Oya) | 4.03 | 🟢 Normal | -0.030 |  |
| 2026-11-05 01:01:57 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:39 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:09 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:09 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-05 01:00:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-11-05 01:00:26 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-05 01:00:18 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.618 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 00:00:26 | Moraketiya (Walawe Ganga) | 4.04 | 🟡 Alert | 1.978 | 🔺 Rising |
| 2026-11-05 01:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-05 00:07:08 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-11-05 00:01:42 | Kuda Oya (Kirindi Oya) | 4.26 | 🟢 Normal | 3.014 | 🔺 Rising |
| 2026-11-05 00:06:49 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-05 00:09:03 | Urawa (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-05 00:07:29 | Thanamalwila (Kirindi Oya) | 3.35 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-05 01:03:33 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-05 01:02:18 | Dunamale (Aththanagalu Oya) | 2.95 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-05 01:03:40 | Giriulla (Maha Oya) | 3.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-05 01:00:26 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-05 00:02:01 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-05 01:03:26 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-05 00:09:42 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-05 01:01:57 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:04:47 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:10:03 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:09 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:03:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:03:19 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:39 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:00:24 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:09 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-05 00:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-11-05 00:09:46 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-11-05 00:03:21 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-05 01:03:19 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.021 |  |
| 2026-11-05 00:01:21 | Holombuwa (Kelani Ganga) | 1.39 | 🟢 Normal | -0.023 |  |
| 2026-11-05 01:03:51 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-05 01:02:03 | Moragaswewa (Deduru Oya) | 4.03 | 🟢 Normal | -0.030 |  |
| 2026-11-05 00:11:22 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 01:00:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-11-05 00:02:22 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.070 |  |
| 2026-11-05 01:03:37 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.088 |  |
| 2026-11-05 00:08:01 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.093 |  |
| 2026-11-05 01:00:18 | Wellawaya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.618 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)