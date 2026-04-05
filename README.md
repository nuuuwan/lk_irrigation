# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_10:12:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,738 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 10:12:44 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.068 |  |
| 2026-04-05 10:12:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.044 |  |
| 2026-04-05 10:11:25 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:09:32 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.009 |  |
| 2026-04-05 10:09:30 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.036 |  |
| 2026-04-05 10:09:15 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-04-05 10:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-04-05 10:08:32 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-05 10:07:26 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.051 |  |
| 2026-04-05 10:07:08 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.040 |  |
| 2026-04-05 10:05:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-05 10:05:27 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 10:05:15 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:05:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:04:58 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:04:56 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:04:39 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.378 |  |
| 2026-04-05 10:04:38 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-04-05 10:04:30 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:02:58 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 10:02:48 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.072 |  |
| 2026-04-05 10:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:02:33 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:02:27 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.051 |  |
| 2026-04-05 10:02:25 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:02:18 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:02:15 | Thanthirimale (Malwathu Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:02:15 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:02:07 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.089 |  |
| 2026-04-05 10:01:45 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-04-05 10:01:40 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:01:29 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.050 |  |
| 2026-04-05 10:01:29 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:01:22 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:01:11 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:01:07 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-05 10:00:55 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-04-05 09:50:23 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:23:36 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 10:02:58 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-05 10:05:51 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-05 10:05:27 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 10:08:32 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-05 10:01:29 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 09:01:46 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:04:58 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:02:33 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:11:25 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:04:56 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:02:18 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:05:15 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:02:25 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:05:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 10:09:32 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.009 |  |
| 2026-04-05 10:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-04-05 10:04:30 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:02:15 | Thanthirimale (Malwathu Oya) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:01:11 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:01:40 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:02:15 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:01:22 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-05 10:01:07 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-04-05 10:00:55 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-04-05 10:04:38 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-04-05 09:23:36 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.023 |  |
| 2026-04-05 10:09:15 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-04-05 10:01:45 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-04-05 10:09:30 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.036 |  |
| 2026-04-05 10:07:08 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.040 |  |
| 2026-04-05 10:12:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.044 |  |
| 2026-04-05 10:01:29 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.050 |  |
| 2026-04-05 10:02:27 | Manampitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.051 |  |
| 2026-04-05 10:07:26 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.051 |  |
| 2026-04-05 10:12:44 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.068 |  |
| 2026-04-05 10:02:48 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.072 |  |
| 2026-04-05 10:02:07 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.089 |  |
| 2026-04-05 10:04:39 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.378 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)