# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_04:15:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 04:15:52 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:10:02 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-05-19 04:08:23 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.028 |  |
| 2026-05-19 04:08:17 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.025 |  |
| 2026-05-19 04:07:39 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.186 |  |
| 2026-05-19 04:07:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:06:54 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:05:24 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.019 |  |
| 2026-05-19 04:04:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:04:39 | Dunamale (Aththanagalu Oya) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-05-19 04:04:19 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:04:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:04:01 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-19 04:03:52 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-05-19 04:03:47 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-19 04:03:06 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-19 04:03:03 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-05-19 04:02:33 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.492 |  |
| 2026-05-19 04:02:23 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 04:01:54 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-05-19 04:01:50 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.005 |  |
| 2026-05-19 04:01:29 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.012 |  |
| 2026-05-19 04:01:20 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:01:13 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-05-19 04:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:00:38 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-05-19 04:00:16 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:00:00 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-05-19 03:53:23 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-19 03:44:18 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.025 |  |
| 2026-05-19 03:27:33 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:25:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | -0.068 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 04:04:01 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-19 03:53:23 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-19 02:01:21 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 04:02:23 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 04:04:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:15:52 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:01:20 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:04:19 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:04:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:07:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:03:47 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:02:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:06:54 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:00:16 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-19 04:01:50 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.005 |  |
| 2026-05-19 04:03:06 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-19 04:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-19 04:01:13 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-05-19 04:01:29 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.012 |  |
| 2026-05-19 04:03:03 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:27:33 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.012 |  |
| 2026-05-19 04:10:02 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-05-19 04:05:24 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.019 |  |
| 2026-05-19 04:04:39 | Dunamale (Aththanagalu Oya) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-05-19 04:03:52 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-05-19 04:01:54 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-05-19 01:03:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-05-19 04:00:00 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-05-19 04:08:17 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.025 |  |
| 2026-05-19 04:08:23 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.028 |  |
| 2026-05-19 04:00:38 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-19 03:25:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | -0.068 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-19 04:07:39 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.186 |  |
| 2026-05-19 04:02:33 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.492 |  |
| 2026-05-19 03:04:36 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -2.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)