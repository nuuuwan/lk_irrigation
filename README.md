# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_18:02:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,709 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 18:02:42 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:39 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:38 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-11-15 18:02:34 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.021 |  |
| 2026-11-15 18:02:34 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.040 |  |
| 2026-11-15 18:02:26 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:19 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:15 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:02:11 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:02:10 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-15 18:02:08 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-15 18:01:47 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:01:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.183 |  |
| 2026-11-15 18:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:29 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.017 |  |
| 2026-11-15 18:01:25 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-11-15 18:01:23 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:01:18 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-15 18:01:13 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:01:10 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:52 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:51:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.183 |  |
| 2026-11-15 17:26:53 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.017 |  |
| 2026-11-15 17:22:29 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 17:13:45 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 17:05:51 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-15 18:01:13 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:01:47 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:48 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:01:23 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:03:41 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:52 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:05:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:02:08 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:04:52 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:11:41 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:16 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:02:26 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:42 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:19 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:39 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:10 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:04:44 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:11 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:02:15 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.011 |  |
| 2026-11-15 17:05:23 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-11-15 18:01:29 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.017 |  |
| 2026-11-15 18:01:18 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:06:32 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:01:59 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 18:01:25 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-11-15 17:04:23 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 18:02:34 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.021 |  |
| 2026-11-15 18:02:38 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-11-15 18:02:10 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-15 17:01:35 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-11-15 18:02:34 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.040 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-15 18:01:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)