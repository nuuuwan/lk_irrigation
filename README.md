# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_03:02:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,111 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 03:02:29 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:28 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.021 |  |
| 2026-11-15 03:02:07 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:04 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:01:51 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:00:44 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:00:34 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:43:33 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 02:02:16 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 02:07:44 | Panadugama (Nilwala Ganga) | 5.01 | 🟡 Alert | -0.027 |  |
| 2026-11-15 02:01:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 02:01:15 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:00:44 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:06:57 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:16:41 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 01:02:51 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:09:41 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:00:34 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:01:51 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:06:03 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:04:23 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:10:18 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:01:52 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | -0.005 |  |
| 2026-11-15 02:06:15 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.009 |  |
| 2026-11-15 02:10:53 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-15 02:04:45 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.010 |  |
| 2026-11-15 02:02:49 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:04 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:29 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:07 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-15 02:04:22 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-15 01:53:08 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.013 |  |
| 2026-11-15 01:03:03 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2026-11-15 02:08:07 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.018 |  |
| 2026-11-15 02:01:08 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-11-15 02:02:26 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-11-15 03:02:28 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.021 |  |
| 2026-11-15 01:07:11 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | -0.030 |  |
| 2026-11-15 02:04:47 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.031 |  |
| 2026-11-15 02:02:35 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-11-15 02:02:26 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.049 |  |
| 2026-11-15 02:43:33 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.051 |  |
| 2026-11-15 01:41:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.55 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)