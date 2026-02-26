# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_22:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 22:03:30 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:03:23 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 22:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:53 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:40 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-26 22:02:36 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:20 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-26 22:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:02:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:35 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:29 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:14 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-26 22:01:11 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:11 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:01:07 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:01:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-02-26 22:00:37 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:00:36 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 21:27:25 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-26 21:26:03 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-26 21:19:06 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:10:16 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-26 21:10:15 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-02-26 21:09:34 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:08:37 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:08:07 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 21:06:19 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 10.835 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-26 22:01:14 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-26 21:07:31 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-26 21:05:56 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-26 21:01:04 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 22:00:36 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 22:03:23 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 22:02:40 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-26 21:26:03 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-26 22:02:20 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-26 22:01:07 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:01:11 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:02:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 22:01:29 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:35 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:03:30 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:19:06 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:53 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:36 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:11 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:02:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:02:14 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:06:30 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:00:37 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-26 20:27:37 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 21:05:49 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:01:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-02-26 21:05:00 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.013 |  |
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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)