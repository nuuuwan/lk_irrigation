# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--13_18:44:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,332 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 18:44:19 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:43:41 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:10:23 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-07-13 18:09:45 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:09:04 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:07:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:07:06 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-07-13 18:06:38 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:06:27 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:06:19 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:05:16 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-13 18:05:01 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:59 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:52 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:04:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:06 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:31 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.120 |  |
| 2026-07-13 18:03:19 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:03:18 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:17 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:15 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:05 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.067 |  |
| 2026-07-13 18:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:56 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:42 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:34 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.120 |  |
| 2026-07-13 18:02:27 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-07-13 18:02:22 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:12 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:04 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:01:56 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.060 |  |
| 2026-07-13 18:01:29 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:01:18 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:01:16 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:00:38 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 18:00:19 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:00:15 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-13 18:05:16 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-13 18:00:38 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-13 18:03:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:44:19 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:06 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:07:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:06:38 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:22 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:34 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:01:29 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:42 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:01:18 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:09:45 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:00:19 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:18 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:01:16 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:04 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:05:01 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:15 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:59 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:03:17 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:10:23 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-07-13 18:07:06 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-07-13 18:06:27 | Glencourse (Kelani Ganga) | 9.24 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:09:04 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:03:19 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:04:52 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:06:19 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:02:56 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-07-13 18:02:27 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-07-13 18:01:56 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.060 |  |
| 2026-07-13 18:00:15 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.061 |  |
| 2026-07-13 18:03:05 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.067 |  |
| 2026-07-13 18:02:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.120 |  |
| 2026-07-13 18:03:31 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)