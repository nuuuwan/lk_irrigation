# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_02:12:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 02:12:04 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-04-25 02:09:02 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.345 |  |
| 2026-04-25 02:08:04 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -36.000 |  |
| 2026-04-25 02:08:02 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -36.000 |  |
| 2026-04-25 02:06:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-25 02:06:06 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.083 |  |
| 2026-04-25 02:05:48 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.013 |  |
| 2026-04-25 02:05:46 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.106 |  |
| 2026-04-25 02:05:05 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.040 |  |
| 2026-04-25 02:05:04 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-25 02:04:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:04:34 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-04-25 02:04:07 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-04-25 02:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:03:15 | Katharagama (Menik Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:03:09 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.080 |  |
| 2026-04-25 02:02:50 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-04-25 02:02:43 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-04-25 02:02:26 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-25 02:02:07 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.072 |  |
| 2026-04-25 02:02:04 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.030 |  |
| 2026-04-25 02:02:02 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 02:01:28 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:01:26 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-25 02:01:06 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:00:48 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.013 |  |
| 2026-04-25 02:00:40 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-04-25 01:37:09 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:31:46 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:27:55 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 01:08:46 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 21.545 | 🔺 Rising |
| 2026-04-25 02:06:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-25 02:01:26 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-25 02:02:02 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 02:01:06 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:01:28 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:04:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:00:42 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:06:06 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:00:11 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:28 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:03:15 | Katharagama (Menik Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:31:46 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 02:02:43 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-04-25 02:04:34 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-04-25 02:02:26 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-25 01:37:09 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-04-25 02:00:48 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.013 |  |
| 2026-04-25 02:05:48 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.013 |  |
| 2026-04-25 02:05:04 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-04-25 02:00:40 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-04-25 02:02:50 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-04-25 01:20:11 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-04-25 02:12:04 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-25 02:02:04 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.030 |  |
| 2026-04-25 02:04:07 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-04-25 02:05:05 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.040 |  |
| 2026-04-25 01:07:31 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-04-25 02:02:07 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.072 |  |
| 2026-04-25 02:03:09 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.080 |  |
| 2026-04-25 02:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.083 |  |
| 2026-04-25 02:05:46 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.106 |  |
| 2026-04-25 02:09:02 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.345 |  |
| 2026-04-24 22:17:29 | Wellawaya (Kirindi Oya) | 0.18 | 🟢 Normal | -8.018 |  |
| 2026-04-25 02:08:04 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)