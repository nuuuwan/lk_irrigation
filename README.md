# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_12:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,163 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **2** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 12:11:57 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.099 |  |
| 2026-05-08 12:10:04 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.037 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 12:03:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-08 12:01:01 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-08 12:03:10 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-08 12:10:04 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-08 12:06:17 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-08 12:01:50 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 12:06:42 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-08 12:01:20 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:10:09 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 12:04:29 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-05-08 12:06:57 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-08 12:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-08 12:02:26 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-08 12:00:29 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-08 12:01:13 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-08 12:02:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-05-08 12:02:43 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-08 12:02:09 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-05-08 12:04:37 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-05-08 12:00:10 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-05-08 12:03:37 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.024 |  |
| 2026-05-08 12:01:40 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.029 |  |
| 2026-05-08 12:02:06 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.030 |  |
| 2026-05-08 12:05:40 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-05-08 12:01:57 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.032 |  |
| 2026-05-08 12:02:06 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.032 |  |
| 2026-05-08 12:05:28 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.038 |  |
| 2026-05-08 12:05:21 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.038 |  |
| 2026-05-08 12:03:49 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | -0.040 |  |
| 2026-05-08 12:01:29 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.041 |  |
| 2026-05-08 12:00:28 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.042 |  |
| 2026-05-08 11:16:13 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.043 |  |
| 2026-05-08 12:05:23 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.044 |  |
| 2026-05-08 12:03:19 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-05-08 12:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.051 |  |
| 2026-05-08 12:04:55 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.051 |  |
| 2026-05-08 12:07:28 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.064 |  |
| 2026-05-08 12:11:57 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -0.099 |  |
| 2026-05-08 12:04:15 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)