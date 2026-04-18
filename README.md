# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_17:10:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,584 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 17:10:13 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-18 17:08:53 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.143 |  |
| 2026-04-18 17:08:19 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-04-18 17:08:05 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:08:04 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:06:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:06:28 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:06:01 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.029 |  |
| 2026-04-18 17:05:46 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:40 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:38 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:35 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:15 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-18 17:05:11 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:04:53 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:04:29 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-04-18 17:04:15 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:03:45 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-04-18 17:03:13 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-18 17:02:53 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 17:02:49 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-04-18 17:02:42 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-04-18 17:02:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.023 |  |
| 2026-04-18 17:01:53 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-18 17:01:36 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:16 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:14 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:12 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-18 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:00 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:00:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.040 |  |
| 2026-04-18 17:00:52 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.052 |  |
| 2026-04-18 17:00:36 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-18 17:00:33 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:00:15 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.150 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 17:10:13 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-18 17:05:15 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-18 17:03:13 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-18 17:01:53 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-18 17:00:36 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-18 17:02:53 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 17:06:28 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:00 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:00:33 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:38 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:35 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:00:33 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:08:05 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:11 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:14 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:06:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:04:29 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:04:15 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:36 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:46 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:01:16 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:03:54 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:05:40 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:08:04 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 16:13:30 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-18 17:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-04-18 17:01:12 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-18 17:03:45 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-04-18 17:08:19 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-04-18 17:02:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.023 |  |
| 2026-04-18 17:06:01 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.029 |  |
| 2026-04-18 17:02:42 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-04-18 17:00:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.040 |  |
| 2026-04-18 17:02:49 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-04-18 17:00:52 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.052 |  |
| 2026-04-18 17:08:53 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.143 |  |
| 2026-04-18 17:00:15 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)