# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_21:27:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,896 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 21:27:25 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:26:03 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-26 21:19:06 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:10:16 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:10:15 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-26 21:09:34 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:08:37 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:08:07 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-02-26 21:07:31 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-26 21:06:52 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:06:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:06:19 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 10.835 | 🔺 Rising |
| 2026-02-26 21:06:11 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:05:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-26 21:05:49 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:05:00 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.013 |  |
| 2026-02-26 21:04:36 | Pitabeddara (Nilwala Ganga) | 0.07 | 🟢 Normal | 10.835 | 🔺 Rising |
| 2026-02-26 21:04:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:04:19 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:04:11 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.014 |  |
| 2026-02-26 21:03:36 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:03:34 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:03:15 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-02-26 21:03:07 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:54 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 21:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:30 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:28 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:02:27 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:14 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:01:41 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-02-26 21:01:30 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.020 |  |
| 2026-02-26 21:01:22 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:01:11 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:01:04 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 21:00:50 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-26 21:00:30 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 21:06:19 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 10.835 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-26 21:00:50 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-26 21:07:31 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-26 21:00:30 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-26 21:05:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-26 21:01:04 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 21:26:03 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-26 21:02:54 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 21:27:25 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:01:22 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:03:07 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:03:36 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:27 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:10:16 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:19:06 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:08:37 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:04:19 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:04:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:14 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:06:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:01:11 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-26 20:27:37 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:04:11 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:05:49 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:06:52 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:09:34 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:03:34 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:02:28 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-02-26 21:03:15 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-02-26 21:01:41 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-02-26 21:05:00 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.013 |  |
| 2026-02-26 21:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.014 |  |
| 2026-02-26 21:08:07 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-02-26 21:01:30 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.020 |  |
| 2026-02-26 21:10:15 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.020 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)