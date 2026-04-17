# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_17:02:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,675 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 17:02:44 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-17 17:02:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:02:25 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.020 |  |
| 2026-04-17 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:02:16 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-17 17:02:15 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-17 17:02:09 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-17 17:02:04 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:02:00 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 17:01:50 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 17:01:32 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 17:01:25 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:01:23 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:55 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:24 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 17:00:17 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:55:07 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:22:39 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-17 16:10:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:09:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 17:02:15 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-04-17 16:22:39 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-17 17:01:32 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 16:06:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-17 17:02:00 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 17:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 16:02:46 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 17:01:50 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 16:00:43 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:02 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:02:04 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:01:25 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:24 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:00 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:01:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:02:46 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:05:13 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:02:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:01:23 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-17 15:06:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:17 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:03:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:55 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 16:05:23 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:04:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:10:22 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:03:34 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:03:24 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-17 17:02:44 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-17 17:02:09 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:06:43 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-17 16:09:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.018 |  |
| 2026-04-17 17:02:25 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.020 |  |
| 2026-04-17 17:02:16 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-17 16:01:59 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.032 |  |
| 2026-04-17 16:04:53 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-04-17 16:06:02 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)