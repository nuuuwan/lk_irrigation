# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_22:02:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,424 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 22:02:35 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:02:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.038 |  |
| 2026-05-09 22:02:14 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:02:12 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-05-09 22:02:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:53 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:47 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:01:33 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.011 |  |
| 2026-05-09 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-09 22:01:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.070 |  |
| 2026-05-09 22:01:01 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:00:15 | Wellawaya (Kirindi Oya) | 3.62 | 🟢 Normal | 1.032 | 🔺 Rising |
| 2026-05-09 21:17:50 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-05-09 21:14:13 | Katharagama (Menik Ganga) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 22:00:15 | Wellawaya (Kirindi Oya) | 3.62 | 🟢 Normal | 1.032 | 🔺 Rising |
| 2026-05-09 21:02:33 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.890 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-09 21:05:53 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-09 21:00:09 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-09 21:09:04 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-09 22:01:53 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-09 21:17:50 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:47 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:01:01 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:02:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-09 21:03:15 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-09 21:02:24 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 22:02:14 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-09 21:14:13 | Katharagama (Menik Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-09 21:01:07 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-09 21:05:41 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-05-09 22:02:35 | Kuda Oya (Kirindi Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:01:42 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-09 21:03:07 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-09 22:01:33 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.011 |  |
| 2026-05-09 21:02:50 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.012 |  |
| 2026-05-09 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-09 21:02:19 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-05-09 22:02:12 | Thanamalwila (Kirindi Oya) | 2.08 | 🟢 Normal | -0.021 |  |
| 2026-05-09 21:07:14 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-05-09 21:02:24 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-05-09 21:03:17 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.024 |  |
| 2026-05-09 21:05:07 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-05-09 22:02:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.038 |  |
| 2026-05-09 21:05:17 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-05-09 21:04:43 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.042 |  |
| 2026-05-09 21:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | -0.049 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 21:02:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-05-09 22:01:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.070 |  |
| 2026-05-09 21:04:16 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.081 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-09 21:01:54 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)