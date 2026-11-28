# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_08:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,768 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 08:02:55 | Kuda Oya (Kirindi Oya) | 2.54 | 🟢 Normal | -0.088 |  |
| 2026-11-28 08:02:48 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-28 08:02:41 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.067 |  |
| 2026-11-28 08:02:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-28 08:02:17 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | -0.138 |  |
| 2026-11-28 08:02:17 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.030 |  |
| 2026-11-28 08:02:08 | Thanamalwila (Kirindi Oya) | 2.23 | 🟢 Normal | -0.049 |  |
| 2026-11-28 08:01:50 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 08:01:47 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-11-28 08:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-28 08:01:06 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.028 |  |
| 2026-11-28 08:00:31 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-28 08:00:12 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-28 07:33:07 | Holombuwa (Kelani Ganga) | 1.52 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 08:02:48 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-28 07:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-11-28 07:17:51 | Panadugama (Nilwala Ganga) | 5.55 | 🟡 Alert | -0.017 |  |
| 2026-11-28 07:04:09 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | -0.030 |  |
| 2026-11-28 07:01:26 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-11-28 07:07:21 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-11-28 07:09:00 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-28 07:12:11 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-28 07:00:16 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-28 07:10:20 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-28 08:01:50 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:01:21 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:06:52 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:00:50 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 07:01:46 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.004 |  |
| 2026-11-28 07:07:24 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-11-28 08:00:31 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-28 07:10:46 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-28 07:01:02 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-28 08:00:12 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-28 08:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-28 08:02:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-28 07:33:07 | Holombuwa (Kelani Ganga) | 1.52 | 🟢 Normal | -0.021 |  |
| 2026-11-28 08:01:06 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.028 |  |
| 2026-11-28 08:02:17 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.030 |  |
| 2026-11-28 08:01:47 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-11-28 07:02:51 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | -0.038 |  |
| 2026-11-28 08:02:08 | Thanamalwila (Kirindi Oya) | 2.23 | 🟢 Normal | -0.049 |  |
| 2026-11-28 07:02:56 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | -0.052 |  |
| 2026-11-28 07:07:02 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.060 |  |
| 2026-11-28 08:02:41 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.067 |  |
| 2026-11-28 07:04:12 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.070 |  |
| 2026-11-28 07:15:19 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-11-28 08:02:55 | Kuda Oya (Kirindi Oya) | 2.54 | 🟢 Normal | -0.088 |  |
| 2026-11-28 07:06:00 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.093 |  |
| 2026-11-28 07:08:34 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.109 |  |
| 2026-11-28 07:07:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.126 |  |
| 2026-11-28 08:02:17 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | -0.138 |  |
| 2026-11-28 07:10:34 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | -0.184 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)