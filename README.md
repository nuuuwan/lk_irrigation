# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_16:16:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,704 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 16:16:08 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:13:25 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:11:20 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-06-10 16:10:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2026-06-10 16:09:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:09:00 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:08:38 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:08:09 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:07:47 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-06-10 16:07:38 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 16:06:11 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:06:04 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 16:06:01 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-06-10 16:06:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:05:56 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:05:31 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:04:09 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:03:58 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 16:03:57 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:03:55 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.050 |  |
| 2026-06-10 16:03:47 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-06-10 16:03:18 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:03:13 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:03:13 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.040 |  |
| 2026-06-10 16:03:01 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 16:02:53 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:42 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:02:40 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:34 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:28 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-10 16:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:02:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:23 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:01:57 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:01:56 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:01:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.060 |  |
| 2026-06-10 16:01:25 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:00:52 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 16:07:38 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 16:03:58 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 16:03:01 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 16:06:04 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 16:01:56 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:01:57 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:23 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:00:52 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:09:00 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:06:00 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:40 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:08:38 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:13:25 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:05:56 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:03:13 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:26 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:06:11 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:03:18 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:02:34 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:08:09 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:01:25 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:16:08 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:09:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:05:31 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 16:07:47 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-06-10 16:04:09 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:02:42 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:03:57 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-10 16:02:28 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-10 16:06:01 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-06-10 16:03:47 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-06-10 16:10:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.026 |  |
| 2026-06-10 16:11:20 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-06-10 16:03:13 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.040 |  |
| 2026-06-10 16:03:55 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.050 |  |
| 2026-06-10 16:01:25 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)