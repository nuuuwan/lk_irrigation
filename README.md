# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_16:30:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 16:30:04 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-17 16:19:27 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:14:53 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-17 16:14:08 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:08:49 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.028 |  |
| 2026-06-17 16:07:52 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-17 16:07:45 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-06-17 16:06:49 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 16:06:34 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-17 16:06:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-17 16:05:56 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-17 16:05:43 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:05:28 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-06-17 16:05:06 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-06-17 16:03:58 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:50 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-17 16:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:25 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:24 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:06 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | -0.053 |  |
| 2026-06-17 16:03:00 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:02:57 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-17 16:02:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-17 16:02:44 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-17 16:02:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:02:20 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 16:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 16:02:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:49 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:31 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 16:01:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 16:01:25 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:14 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:07 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.011 |  |
| 2026-06-17 16:01:05 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:00 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:00:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:00:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 16:05:28 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-06-17 16:05:06 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-06-17 16:14:53 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-17 16:03:50 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-17 16:02:57 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-17 16:05:56 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-17 16:07:52 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-17 16:06:34 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-17 16:01:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 16:30:04 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-17 16:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 16:06:49 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 16:02:20 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 16:03:58 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:00:07 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:00 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:49 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:19:27 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 15:00:15 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:25 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:03:24 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:14:08 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:25 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:05 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:02:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:05:43 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:01:14 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:02:41 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:00:51 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 16:07:45 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-06-17 16:06:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-17 16:02:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-17 16:01:31 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 16:02:44 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-17 16:01:07 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.011 |  |
| 2026-06-17 16:08:49 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.028 |  |
| 2026-06-17 16:03:06 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)