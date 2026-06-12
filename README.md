# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_14:18:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,426 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 14:18:57 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 14:10:01 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | -0.027 |  |
| 2026-06-12 14:09:24 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.056 |  |
| 2026-06-12 14:07:04 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.057 |  |
| 2026-06-12 14:06:43 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:06:26 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-06-12 14:05:30 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:05:07 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.097 |  |
| 2026-06-12 14:04:44 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.051 |  |
| 2026-06-12 14:04:41 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:04:36 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 14:04:22 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 14:04:06 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:03:45 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-06-12 14:03:44 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.091 |  |
| 2026-06-12 14:03:30 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.046 |  |
| 2026-06-12 14:03:20 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:03:17 | Rathnapura (Kalu Ganga) | 5.36 | 🟡 Alert | -0.084 |  |
| 2026-06-12 14:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:02:59 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:02:54 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.060 |  |
| 2026-06-12 14:02:49 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:02:41 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 14:02:37 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:02:34 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 14:02:25 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.77 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-12 14:02:16 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:02:10 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-06-12 14:02:09 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 14:01:57 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:01:51 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | 0.987 | 🔺 Rising |
| 2026-06-12 14:01:51 | Ellagawa (Kalu Ganga) | 8.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 14:01:44 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:01:35 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-06-12 14:01:14 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:01:06 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:01:04 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-06-12 14:00:38 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 13:59:32 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 13:44:09 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | 0.188 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 14:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.77 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-12 14:10:01 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | -0.027 |  |
| 2026-06-12 14:03:17 | Rathnapura (Kalu Ganga) | 5.36 | 🟡 Alert | -0.084 |  |
| 2026-06-12 14:01:51 | Moraketiya (Walawe Ganga) | 1.58 | 🟢 Normal | 0.987 | 🔺 Rising |
| 2026-06-12 14:06:26 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-06-12 14:01:04 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-06-12 14:18:57 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 14:04:36 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 14:02:09 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 14:01:51 | Ellagawa (Kalu Ganga) | 8.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 14:02:34 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 14:02:41 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 14:04:22 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 14:02:25 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-12 13:59:32 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:04:41 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:00:38 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:02:49 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:01:14 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:03:20 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:02:59 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:02:16 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:01:06 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:06:43 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:01:57 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-12 14:05:30 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:01:44 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:02:37 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-06-12 14:01:35 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-06-12 14:02:10 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-06-12 14:03:45 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-06-12 14:03:30 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.046 |  |
| 2026-06-12 14:04:44 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.051 |  |
| 2026-06-12 14:09:24 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.056 |  |
| 2026-06-12 14:07:04 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.057 |  |
| 2026-06-12 14:02:54 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.060 |  |
| 2026-06-12 14:03:44 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.091 |  |
| 2026-06-12 14:05:07 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)