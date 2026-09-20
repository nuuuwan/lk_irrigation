# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_23:22:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,444 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Dunamale — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Glencourse — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 23:22:38 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-20 23:17:39 | Putupaula (Kalu Ganga) | 2.24 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-20 23:12:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 23:03:57 | Panadugama (Nilwala Ganga) | 6.25 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-09-20 23:02:44 | Dunamale (Aththanagalu Oya) | 3.38 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-09-20 23:07:03 | Baddegama (Gin Ganga) | 3.68 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-09-20 23:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-09-20 23:03:54 | Magura (Kalu Ganga) | 5.60 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-20 23:04:09 | Glencourse (Kelani Ganga) | 15.60 | 🟡 Alert | 0.000 |  |
| 2026-09-20 23:02:33 | Thawalama (Gin Ganga) | 5.45 | 🟡 Alert | -0.031 |  |
| 2026-09-20 23:04:34 | Rathnapura (Kalu Ganga) | 6.50 | 🟡 Alert | -0.053 |  |
| 2026-09-20 23:06:01 | Norwood (Kelani Ganga) | 1.58 | 🟡 Alert | -0.067 |  |
| 2026-09-20 23:00:22 | Peradeniya (Mahaweli Ganga) | 5.13 | 🟡 Alert | -0.075 |  |
| 2026-09-20 23:05:46 | Badalgama (Maha Oya) | 4.09 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-09-20 23:08:59 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-09-20 23:03:42 | Hanwella (Kelani Ganga) | 6.72 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-20 23:02:23 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-20 23:03:47 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 23:17:39 | Putupaula (Kalu Ganga) | 2.24 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-20 23:22:38 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-20 23:01:51 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 23:06:56 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-20 23:01:02 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 23:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 23:01:28 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 23:12:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 23:07:27 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-20 23:03:05 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 23:02:20 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 23:06:44 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-09-20 23:02:19 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-20 23:04:09 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 23:02:15 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.022 |  |
| 2026-09-20 23:02:00 | Pitabeddara (Nilwala Ganga) | 2.77 | 🟢 Normal | -0.029 |  |
| 2026-09-20 23:06:12 | Urawa (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.063 |  |
| 2026-09-20 23:03:25 | Deraniyagala (Kelani Ganga) | 2.56 | 🟢 Normal | -0.080 |  |
| 2026-09-20 23:02:15 | Giriulla (Maha Oya) | 3.54 | 🟢 Normal | -0.093 |  |
| 2026-09-20 23:01:35 | Nawalapitiya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.219 |  |
| 2026-09-20 23:08:57 | Holombuwa (Kelani Ganga) | 2.58 | 🟢 Normal | -0.324 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)