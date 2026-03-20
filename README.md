# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_22:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,857 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 22:11:11 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:10:54 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:09:12 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.113 |  |
| 2026-03-20 22:08:38 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:08:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:07:38 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:07:16 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:07:13 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:06:40 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 22:06:16 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:06:02 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-03-20 22:05:13 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-20 22:04:55 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.039 |  |
| 2026-03-20 22:04:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-20 22:04:46 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 22:04:04 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-03-20 22:03:45 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:03:36 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:03:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:03:12 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:02:35 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:02:32 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-03-20 22:02:27 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:02:09 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-20 22:02:08 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-20 22:02:04 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:02:03 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.557 |  |
| 2026-03-20 22:01:52 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:01:50 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-03-20 22:01:48 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:01:38 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:01:35 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.021 |  |
| 2026-03-20 22:00:52 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:59:58 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 22:01:50 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-03-20 22:02:32 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-03-20 22:02:09 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-20 22:06:40 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 22:02:08 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-20 22:05:13 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 22:04:46 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 22:00:52 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:07:16 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 21:03:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:02:04 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:06:16 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:03:12 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:01:52 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:03:36 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:02:27 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:11:11 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:10:54 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:03:45 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:08:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:01:48 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:07:38 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:08:38 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:07:13 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:03:14 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:02:35 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:01:38 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-20 22:04:04 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.011 |  |
| 2026-03-20 22:06:02 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-03-20 22:01:35 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.021 |  |
| 2026-03-20 21:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-03-20 22:04:55 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.039 |  |
| 2026-03-20 22:04:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-20 22:09:12 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.113 |  |
| 2026-03-20 22:02:03 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.557 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)