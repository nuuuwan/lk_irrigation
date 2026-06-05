# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_18:21:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,334 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 18:21:15 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:16:25 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:14:01 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:11:19 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 18:09:33 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:07:59 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:47 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:05 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.019 |  |
| 2026-06-05 18:05:52 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:05:25 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-06-05 18:05:15 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-05 18:04:57 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-05 18:04:35 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:04:19 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:04:10 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:03:54 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:03:38 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 18:03:31 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 18:03:31 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.023 |  |
| 2026-06-05 18:03:14 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-05 18:03:14 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.042 |  |
| 2026-06-05 18:03:09 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-05 18:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:02:39 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 18:02:19 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.024 |  |
| 2026-06-05 18:02:05 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.040 |  |
| 2026-06-05 18:02:02 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.011 |  |
| 2026-06-05 18:01:53 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:01:49 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-05 18:01:38 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.025 |  |
| 2026-06-05 18:01:26 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-05 18:01:26 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 18:01:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.013 |  |
| 2026-06-05 18:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:01:06 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 17:47:17 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 18:04:57 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-05 18:06:47 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-05 18:03:09 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-05 18:05:15 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-05 18:03:31 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 18:01:26 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-06-05 18:03:38 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 18:02:39 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 18:11:19 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 18:04:10 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:01:26 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:01:53 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:16:25 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:14:01 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:01:06 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:04:35 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:05:52 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:09:33 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:21:15 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:01:49 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:03:54 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:05:25 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-06-05 18:04:19 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-06-05 17:02:27 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:02:02 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.011 |  |
| 2026-06-05 18:01:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.013 |  |
| 2026-06-05 18:06:05 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.019 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-05 17:04:44 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-06-05 18:03:31 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.023 |  |
| 2026-06-05 18:02:19 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.024 |  |
| 2026-06-05 18:01:38 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.025 |  |
| 2026-06-05 18:03:14 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.030 |  |
| 2026-06-05 18:02:05 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.040 |  |
| 2026-06-05 18:03:14 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)