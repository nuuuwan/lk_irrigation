# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_18:09:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,470 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 18:09:29 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-25 18:08:54 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-25 18:07:10 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:06:56 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | -0.040 |  |
| 2026-05-25 18:06:17 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-25 18:05:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:05:21 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:56 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:55 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-05-25 18:04:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:34 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:20 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:16 | Hanwella (Kelani Ganga) | 4.31 | 🟢 Normal | -0.101 |  |
| 2026-05-25 18:04:08 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 18:04:06 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-05-25 18:04:01 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.040 |  |
| 2026-05-25 18:03:11 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:03:03 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:02:59 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.029 |  |
| 2026-05-25 18:02:57 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:57 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:38 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:02:31 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:15 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 18:02:14 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:08 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:01:35 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:01:30 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:01:17 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-25 18:00:57 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-25 18:00:22 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 18:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.040 |  |
| 2026-05-25 18:01:17 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-25 18:06:17 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-25 18:09:29 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-25 18:08:54 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-25 18:00:57 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-25 18:02:15 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 18:01:35 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 18:04:08 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 18:04:34 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:20 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:35 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:07:10 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:57 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:05:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:31 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:01:30 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:14 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:57 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:01 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:05:21 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:04:56 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:02:08 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 18:01:32 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:23 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:03:11 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.010 |  |
| 2026-05-25 18:02:07 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:02:38 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-05-25 18:04:55 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.019 |  |
| 2026-05-25 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:03:03 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.020 |  |
| 2026-05-25 18:04:06 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-05-25 18:00:22 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | -0.021 |  |
| 2026-05-25 18:02:59 | Deraniyagala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.029 |  |
| 2026-05-25 18:06:56 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | -0.040 |  |
| 2026-05-25 17:03:51 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-05-25 18:04:16 | Hanwella (Kelani Ganga) | 4.31 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)