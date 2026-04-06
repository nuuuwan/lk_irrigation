# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_18:02:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,920 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 18:02:51 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-06 18:02:40 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-06 18:02:36 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.082 |  |
| 2026-04-06 18:02:22 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:02:19 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:02:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 18:01:46 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:01:32 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 18:01:25 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:55 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:52 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:19:57 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-06 17:18:17 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:12:29 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:10:03 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-04-06 17:08:56 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-06 17:08:54 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 17:10:03 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-04-06 17:07:11 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-04-06 18:01:32 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-06 18:02:51 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-06 18:02:40 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-06 17:19:57 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-06 18:02:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-06 17:08:54 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 18:02:19 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 18:00:52 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 16:01:41 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:25 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:12:29 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:01:18 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:07:37 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:17 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:49 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:02:22 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:02:03 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:03:45 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:55 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-06 17:06:59 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-06 17:06:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:18:17 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:00:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:03:51 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:25 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-06 17:05:47 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-06 16:03:46 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:01:46 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:01:44 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-06 17:04:17 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 18:02:36 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)