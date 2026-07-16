# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_08:06:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,606 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 08:06:30 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-07-16 08:05:57 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:05:52 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:05:48 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 08:05:30 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-07-16 08:05:16 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-07-16 08:05:16 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:53 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:47 | Nagalagam Street (Kelani Ganga) | 0.02 | 🟢 Normal | -0.081 |  |
| 2026-07-16 08:04:36 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:28 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:22 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:05 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:03:53 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | -0.020 |  |
| 2026-07-16 08:03:41 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:03:27 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:03:26 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:03:11 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-07-16 08:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -3.429 |  |
| 2026-07-16 08:02:38 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-16 08:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -3.429 |  |
| 2026-07-16 08:02:32 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:02:25 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:01:34 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 08:01:33 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.032 |  |
| 2026-07-16 08:01:31 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:01:29 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-16 08:01:23 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.140 |  |
| 2026-07-16 08:00:55 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:00:17 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-16 07:41:17 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 07:37:13 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 07:33:25 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 08:05:30 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-07-16 08:00:17 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-16 08:02:38 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-07-16 08:01:29 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-16 08:05:48 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 08:01:34 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 07:41:17 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:05:57 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:02:32 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:01:23 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:05 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:22 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:03:27 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:28 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:03:41 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:03:26 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-16 07:33:25 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-07-16 06:04:58 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:02:25 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:53 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:05:52 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-16 07:03:16 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:01:31 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-16 07:05:16 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:04:36 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 08:05:16 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-16 07:08:30 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-07-16 08:05:16 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-07-16 08:06:30 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-07-16 07:04:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-07-16 08:03:53 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | -0.020 |  |
| 2026-07-16 07:08:10 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-07-16 08:03:11 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-07-16 08:01:33 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.032 |  |
| 2026-07-16 07:01:25 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.062 |  |
| 2026-07-16 08:04:47 | Nagalagam Street (Kelani Ganga) | 0.02 | 🟢 Normal | -0.081 |  |
| 2026-07-16 08:01:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.140 |  |
| 2026-07-16 08:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -3.429 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)