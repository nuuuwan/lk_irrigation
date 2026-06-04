# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_22:19:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 22:19:16 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-04 22:16:49 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.110 |  |
| 2026-06-04 22:15:19 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:12:21 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-04 22:12:11 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-04 22:11:46 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.009 |  |
| 2026-06-04 22:10:24 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.037 |  |
| 2026-06-04 22:09:59 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:07:52 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.038 |  |
| 2026-06-04 22:06:45 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-06-04 22:06:10 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-06-04 22:06:05 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-04 22:06:02 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-04 22:05:11 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:04:44 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:04:26 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-04 22:04:19 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 22:04:16 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:04:09 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-04 22:03:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:03:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:03:36 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:03:20 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.200 |  |
| 2026-06-04 22:03:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 22:02:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:02:35 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:02:26 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 22:02:20 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-04 22:02:11 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:02:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:01:41 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:01:30 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.044 |  |
| 2026-06-04 22:01:21 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-06-04 22:00:34 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 22:02:20 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-04 22:12:21 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-04 21:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-04 22:04:26 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-04 22:06:05 | Ellagawa (Kalu Ganga) | 6.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-04 22:12:11 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-04 22:06:02 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-04 22:02:26 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-04 22:00:34 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 22:04:19 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 22:03:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 22:19:16 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-04 22:03:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:04:44 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:03:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:15:19 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:02:35 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:02:11 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:02:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 21:02:14 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:04:16 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:02:10 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:03:36 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:09:59 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:01:41 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 22:11:46 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.009 |  |
| 2026-06-04 22:06:45 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-06-04 21:12:47 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.017 |  |
| 2026-06-04 22:06:10 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-06-04 22:01:21 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-06-04 22:04:09 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-04 22:10:24 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.037 |  |
| 2026-06-04 22:07:52 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.038 |  |
| 2026-06-04 22:01:30 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.044 |  |
| 2026-06-04 22:16:49 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.110 |  |
| 2026-06-04 22:03:20 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)