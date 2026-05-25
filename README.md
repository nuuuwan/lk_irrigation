# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_13:23:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 13:23:57 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-05-25 13:16:02 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:15:58 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-05-25 13:14:02 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-05-25 13:13:21 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 13:08:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-05-25 13:07:50 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:06:39 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.031 |  |
| 2026-05-25 13:06:37 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.126 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 13:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | -0.057 |  |
| 2026-05-25 13:02:50 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-25 13:02:00 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 13:01:25 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 13:13:21 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-25 13:05:33 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 13:03:03 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:01:14 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:02:42 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:00:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:03:05 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:01:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:16:02 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:01:26 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:02:00 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:54 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:02:57 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:07:50 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:05:41 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:05:42 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:01:54 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:00:39 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:06:04 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:04:04 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:02:42 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 13:15:58 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-05-25 13:14:02 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-05-25 13:03:57 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-05-25 13:01:50 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-05-25 13:03:52 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | -0.019 |  |
| 2026-05-25 13:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-05-25 13:23:57 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-05-25 13:08:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-05-25 13:06:39 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.031 |  |
| 2026-05-25 13:03:19 | Hanwella (Kelani Ganga) | 4.77 | 🟢 Normal | -0.080 |  |
| 2026-05-25 13:05:49 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.085 |  |
| 2026-05-25 13:02:25 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.103 |  |
| 2026-05-25 13:06:37 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.126 |  |
| 2026-05-25 13:02:21 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | -209.455 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)