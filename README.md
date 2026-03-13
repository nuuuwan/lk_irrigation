# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_23:24:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 23:24:02 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.016 |  |
| 2026-03-13 23:08:42 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:08:17 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-13 23:07:45 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 23:06:52 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-13 23:06:10 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 23:05:57 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-13 23:05:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-03-13 23:05:04 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 23:05:03 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 23:05:00 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:04:58 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:04:55 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 23:04:38 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:04:36 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-13 23:04:10 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:03:55 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.048 |  |
| 2026-03-13 23:03:06 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-13 23:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.050 |  |
| 2026-03-13 23:02:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-03-13 23:02:49 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:31 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-03-13 23:02:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:21 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:11 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.266 |  |
| 2026-03-13 23:02:10 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:02 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:01:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-13 23:01:21 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-13 23:01:09 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 23:08:17 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-13 23:04:36 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-13 23:06:52 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-13 23:03:06 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-13 23:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-13 23:05:03 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 23:06:10 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 23:01:21 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-13 23:04:55 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 23:05:04 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 23:07:45 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 22:01:30 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:06:41 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:01:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:26 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:13:35 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:06:56 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:02 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:49 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:05:00 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:04:38 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:10 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:02:21 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:04:10 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:08:42 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:05:57 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-13 22:06:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-13 23:24:02 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.016 |  |
| 2026-03-13 23:02:31 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-03-13 23:01:09 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-03-13 23:02:59 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-03-13 23:03:55 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.048 |  |
| 2026-03-13 23:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.050 |  |
| 2026-03-13 23:05:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.059 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-13 23:02:11 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.266 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)