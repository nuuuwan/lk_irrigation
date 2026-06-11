# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_05:16:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 05:16:43 | Ellagawa (Kalu Ganga) | 7.63 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 05:15:11 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-12 05:14:11 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-12 05:13:17 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 05:11:12 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-06-12 05:10:57 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-06-12 05:10:49 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-06-12 05:10:23 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.028 |  |
| 2026-06-12 05:09:44 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-12 05:08:50 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.829 |  |
| 2026-06-12 05:06:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:05:57 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 05:05:54 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-12 05:04:54 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 05:03:52 | Rathnapura (Kalu Ganga) | 5.85 | 🟡 Alert | 0.135 | 🔺 Rising |
| 2026-06-12 05:03:32 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:03:06 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-12 05:02:56 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.060 |  |
| 2026-06-12 05:02:52 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:48 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:47 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:21 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-12 05:02:19 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.829 |  |
| 2026-06-12 05:02:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:08 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:01:40 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-06-12 05:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.020 |  |
| 2026-06-12 05:01:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:01:10 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:00:50 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:51:41 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.314 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 05:11:12 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-06-12 05:03:52 | Rathnapura (Kalu Ganga) | 5.85 | 🟡 Alert | 0.135 | 🔺 Rising |
| 2026-06-12 05:10:49 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-06-12 05:10:57 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-06-12 04:12:14 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-06-12 05:15:11 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-12 05:03:06 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-12 04:07:33 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-12 05:02:21 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-12 05:09:44 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-12 05:05:54 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-12 05:14:11 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-12 04:02:32 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-12 05:16:43 | Ellagawa (Kalu Ganga) | 7.63 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 05:05:57 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 05:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 05:13:17 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 04:06:05 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 05:02:47 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:00:50 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:03:32 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:48 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:01:20 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:06:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:01:10 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:04:54 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:12:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:52 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:02:08 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-12 05:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.020 |  |
| 2026-06-12 05:01:40 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-12 05:10:23 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.028 |  |
| 2026-06-12 04:05:35 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.048 |  |
| 2026-06-12 05:02:56 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.060 |  |
| 2026-06-12 05:08:50 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.829 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)