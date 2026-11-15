# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_23:30:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,900 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 23:30:52 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.023 |  |
| 2026-11-15 23:26:46 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:10:47 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:09:21 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:07:44 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:05:57 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:05:42 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.012 |  |
| 2026-11-15 23:05:33 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | -0.010 |  |
| 2026-11-15 23:05:09 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-11-15 23:04:19 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:03:55 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-11-15 23:03:49 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:03:49 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-11-15 23:03:14 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-15 23:02:59 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:57 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-11-15 23:02:43 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:35 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:29 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:20 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:19 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:15 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:01:59 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:01:57 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.042 |  |
| 2026-11-15 23:01:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:01:42 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:01:35 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:01:12 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-11-15 23:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:00:05 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:56:33 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 23:05:33 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | -0.010 |  |
| 2026-11-15 23:03:14 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-15 22:01:34 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:01:50 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:07:44 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:59 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:06:10 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:19 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:29 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:01:42 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:04:19 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:01:35 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:43 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:00:05 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:20 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:59 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:10:47 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:26:46 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:02:35 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-15 23:09:21 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:05:57 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:03:49 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:01:59 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:02:15 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-15 23:01:12 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-15 23:03:55 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-11-15 23:05:42 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.012 |  |
| 2026-11-15 22:10:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.018 |  |
| 2026-11-15 22:05:43 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-11-15 23:03:49 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-11-15 23:05:09 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-11-15 23:02:57 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-11-15 23:30:52 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.023 |  |
| 2026-11-15 22:17:44 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.027 |  |
| 2026-11-15 23:01:57 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.042 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)