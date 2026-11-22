# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_10:03:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 10:03:28 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.106 |  |
| 2026-11-22 10:03:07 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:54 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:34 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:32 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-22 10:02:22 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.021 |  |
| 2026-11-22 10:02:14 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:04 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-11-22 10:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:01:49 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-22 10:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:01:05 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:00:10 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:00:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 10:01:49 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-22 10:02:32 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-22 09:03:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-22 09:04:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-22 09:02:21 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 09:03:34 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 09:00:46 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 10:00:10 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:02:10 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:07 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:16:01 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:01:05 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 10:00:09 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:07:57 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:05:09 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:07:13 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:08:16 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-22 10:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:34 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:54 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:03:07 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:14 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:03:54 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:00:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-22 10:02:22 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:01:20 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-11-22 09:08:51 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.011 |  |
| 2026-11-22 09:01:00 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.012 |  |
| 2026-11-22 09:03:34 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-11-22 09:04:23 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-22 10:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.021 |  |
| 2026-11-22 10:02:04 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-11-22 09:05:09 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-22 09:03:51 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.046 |  |
| 2026-11-22 09:06:31 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.056 |  |
| 2026-11-22 10:03:28 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)