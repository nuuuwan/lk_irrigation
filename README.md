# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_08:06:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,996 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 08:06:57 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:06:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.020 |  |
| 2026-07-31 08:05:46 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.317 |  |
| 2026-07-31 08:05:40 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.026 |  |
| 2026-07-31 08:05:22 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 08:05:18 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.117 |  |
| 2026-07-31 08:04:36 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:04:19 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:04:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:04:00 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-31 08:03:27 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:03:14 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 08:03:12 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:02:55 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:02:52 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:02:47 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-07-31 08:02:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-31 08:01:55 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:01:51 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 08:01:45 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.055 |  |
| 2026-07-31 08:01:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:01:41 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:01:33 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:00:56 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:00:46 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:00:20 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-31 07:34:02 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 07:31:26 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 07:25:09 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 07:24:32 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 07:23:11 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-31 07:19:05 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 08:00:20 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-31 07:01:14 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-07-31 08:05:22 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 07:05:42 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 08:01:51 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 07:34:02 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-31 07:10:17 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-31 08:03:14 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 08:02:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:02:47 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:03:12 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 08:06:57 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 07:01:38 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.003 |  |
| 2026-07-31 08:01:41 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:02:55 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:01:42 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:03:27 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 07:25:09 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:04:19 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:04:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:04:36 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:00:56 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:01:55 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:00:46 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 07:09:06 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-31 07:23:11 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:01:33 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:02:52 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 08:04:00 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-31 08:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-31 08:06:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | -0.020 |  |
| 2026-07-31 07:13:02 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-07-31 07:03:27 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.021 |  |
| 2026-07-31 08:05:40 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.026 |  |
| 2026-07-31 08:01:45 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.055 |  |
| 2026-07-31 08:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-07-31 07:06:12 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.091 |  |
| 2026-07-31 08:05:18 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.117 |  |
| 2026-07-31 08:05:46 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.317 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)