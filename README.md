# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_16:14:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 16:14:05 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:13:42 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:09:48 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-05 16:09:17 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.055 |  |
| 2026-06-05 16:08:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:08:11 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:06:56 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 16:06:28 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.096 |  |
| 2026-06-05 16:06:10 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 16:06:06 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-06-05 16:05:57 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.073 |  |
| 2026-06-05 16:05:51 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.031 |  |
| 2026-06-05 16:05:06 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:42 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-05 16:03:41 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-06-05 16:03:36 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:25 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-05 16:03:21 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.023 |  |
| 2026-06-05 16:03:19 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-06-05 16:03:00 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 16:02:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-05 16:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-06-05 16:02:31 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 16:02:28 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-06-05 16:02:28 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 16:02:12 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.040 |  |
| 2026-06-05 16:01:52 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-06-05 16:01:50 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -114.000 |  |
| 2026-06-05 16:01:40 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:39 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-06-05 16:01:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:31 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:26 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -114.000 |  |
| 2026-06-05 16:01:16 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:14 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 16:00:39 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:00:30 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:00:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 16:02:47 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-05 16:09:48 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-05 16:03:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-05 15:02:30 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-05 16:03:00 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 16:06:10 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 16:02:28 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-05 16:01:14 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 16:02:31 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 16:06:56 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-05 16:03:36 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:00:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:14:05 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:00:39 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:05:06 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:31 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:19 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:40 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:01:16 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:08:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:08:11 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-05 15:04:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-05 16:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-06-05 16:01:39 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-06-05 16:06:06 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-06-05 16:01:52 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-06-05 16:02:28 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-06-05 16:03:41 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-06-05 16:03:21 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.023 |  |
| 2026-06-05 16:05:51 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -0.031 |  |
| 2026-06-05 16:02:35 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-06-05 16:03:42 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-05 16:02:12 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.040 |  |
| 2026-06-05 16:09:17 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.055 |  |
| 2026-06-05 16:05:57 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.073 |  |
| 2026-06-05 16:06:28 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.096 |  |
| 2026-06-05 16:01:50 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -114.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)