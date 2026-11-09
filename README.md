# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_08:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,919 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 08:03:25 | Ellagawa (Kalu Ganga) | 7.91 | 🟢 Normal | -0.055 |  |
| 2026-11-09 08:03:23 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 08:02:55 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.029 |  |
| 2026-11-09 08:02:46 | Badalgama (Maha Oya) | 4.52 | 🟢 Normal | -0.075 |  |
| 2026-11-09 08:02:31 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-11-09 08:02:15 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:02:15 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-11-09 08:02:09 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-09 08:02:00 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.069 |  |
| 2026-11-09 08:01:45 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:01:44 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-11-09 08:01:39 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-11-09 08:01:28 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | -0.131 |  |
| 2026-11-09 08:01:00 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:00:58 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-11-09 08:00:55 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-11-09 08:00:41 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-09 07:35:33 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-11-09 07:33:26 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.062 |  |
| 2026-11-09 07:25:17 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.081 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 07:03:27 | Dunamale (Aththanagalu Oya) | 4.32 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-11-09 07:13:10 | Magura (Kalu Ganga) | 5.30 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-11-09 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 07:13:39 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-11-09 07:01:16 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-09 07:21:15 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | -0.015 |  |
| 2026-11-09 08:01:39 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-11-09 07:08:12 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-09 08:03:23 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 07:02:22 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-09 07:08:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:03:23 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:08:04 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:01:45 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:02:15 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:01:00 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-09 08:02:09 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-11-09 08:00:58 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-11-09 08:02:31 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 07:00:43 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-11-09 08:02:55 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.029 |  |
| 2026-11-09 08:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-09 08:02:15 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-11-09 08:01:44 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-11-09 07:16:56 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.035 |  |
| 2026-11-09 08:00:55 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-11-09 08:03:25 | Ellagawa (Kalu Ganga) | 7.91 | 🟢 Normal | -0.055 |  |
| 2026-11-09 07:33:26 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.062 |  |
| 2026-11-09 07:04:19 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |
| 2026-11-09 08:02:00 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.069 |  |
| 2026-11-09 08:02:46 | Badalgama (Maha Oya) | 4.52 | 🟢 Normal | -0.075 |  |
| 2026-11-09 07:25:17 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.081 |  |
| 2026-11-09 08:01:28 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | -0.131 |  |
| 2026-11-09 07:04:16 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.142 |  |
| 2026-11-09 07:05:11 | Hanwella (Kelani Ganga) | 5.04 | 🟢 Normal | -0.145 |  |
| 2026-11-09 07:01:35 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.172 |  |
| 2026-11-09 07:06:10 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.183 |  |
| 2026-11-09 07:02:51 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.291 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)