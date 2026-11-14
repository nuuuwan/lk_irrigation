# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_07:04:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,366 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 07:04:12 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.072 |  |
| 2026-11-14 07:04:07 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2026-11-14 07:03:59 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-14 07:03:41 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:03:41 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2026-11-14 07:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.105 |  |
| 2026-11-14 07:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-11-14 07:02:59 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:02:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.122 |  |
| 2026-11-14 07:02:32 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:02:31 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-14 07:02:12 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:56 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:46 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.102 |  |
| 2026-11-14 07:01:39 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.517 |  |
| 2026-11-14 07:01:25 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:20 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:14 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-14 07:00:58 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | -0.018 |  |
| 2026-11-14 07:00:39 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-14 07:00:30 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-14 06:34:56 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 06:01:24 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | -0.026 |  |
| 2026-11-14 06:08:31 | Baddegama (Gin Ganga) | 3.73 | 🟡 Alert | -0.036 |  |
| 2026-11-14 06:06:56 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.076 |  |
| 2026-11-14 07:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.105 |  |
| 2026-11-14 07:00:30 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-14 06:01:33 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-14 06:05:52 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 06:01:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:25 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:03:41 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:20 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:01:56 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:04:36 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:00:47 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 06:01:33 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:02:12 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:02:32 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 07:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-11-14 07:04:07 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2026-11-14 07:02:31 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-14 07:01:14 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-11-14 06:01:38 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-14 06:34:56 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-11-14 06:12:30 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.017 |  |
| 2026-11-14 07:00:58 | Thanthirimale (Malwathu Oya) | 1.69 | 🟢 Normal | -0.018 |  |
| 2026-11-14 06:02:43 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-11-14 07:00:39 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-14 07:03:59 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-14 06:00:32 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-11-14 06:01:14 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.023 |  |
| 2026-11-14 06:06:58 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.029 |  |
| 2026-11-14 06:14:08 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-11-14 07:03:41 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2026-11-14 06:10:05 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.063 |  |
| 2026-11-14 06:02:33 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.066 |  |
| 2026-11-14 07:04:12 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.072 |  |
| 2026-11-14 07:01:46 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.102 |  |
| 2026-11-14 07:02:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.122 |  |
| 2026-11-14 07:01:39 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.517 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)