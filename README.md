# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_14:40:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 14:40:50 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:13:11 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:10:23 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:09:44 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-28 14:09:20 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:08:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:08:35 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-06-28 14:06:59 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-28 14:06:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:05:34 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:04:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:04:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-28 14:04:00 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.012 |  |
| 2026-06-28 14:03:53 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:03:28 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:03:27 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:03:23 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-06-28 14:03:21 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-28 14:03:15 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-06-28 14:03:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-28 14:02:58 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-28 14:02:45 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:31 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:28 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:15 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:01 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:01 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:01:59 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.019 |  |
| 2026-06-28 14:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:01:47 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:01:28 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:11 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:08 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:08 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:00:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:00:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:00:42 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:59:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 14:03:23 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-06-28 14:02:58 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-28 14:04:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-28 14:06:59 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-28 14:03:21 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-28 14:03:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-28 14:09:44 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-28 14:02:15 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:00:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:03:27 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:00:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:01 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:13:11 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:40:50 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:03:53 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:03:28 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:01 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:45 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:01:08 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-28 13:59:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:31 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:02:28 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:00:42 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:05:34 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:06:17 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:10:23 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:04:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:08:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-28 14:09:20 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:11 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:47 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:28 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:01:08 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-28 14:04:00 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.012 |  |
| 2026-06-28 14:01:59 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.019 |  |
| 2026-06-28 14:03:15 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-06-28 14:08:35 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)