# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_15:09:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 15:09:33 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:09:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.037 |  |
| 2026-05-10 15:09:25 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.028 |  |
| 2026-05-10 15:08:26 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.028 |  |
| 2026-05-10 15:07:51 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-10 15:07:49 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:07:47 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:07:46 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.019 |  |
| 2026-05-10 15:07:19 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.064 |  |
| 2026-05-10 15:06:59 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-05-10 15:06:48 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:06:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:06:19 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-10 15:06:13 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:05:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:05:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-10 15:04:36 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.040 |  |
| 2026-05-10 15:04:04 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-05-10 15:03:56 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 15:03:30 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:03:18 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 15:03:17 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 15:03:00 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:03:00 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.023 |  |
| 2026-05-10 15:02:57 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:02:41 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:02:31 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-05-10 15:02:28 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:02:24 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.050 |  |
| 2026-05-10 15:02:13 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:02:10 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:57 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-05-10 15:01:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 15:01:33 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:25 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:01:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:15 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:25:43 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 15:07:51 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-10 15:05:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-10 15:01:57 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 15:03:17 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 15:03:18 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 15:03:56 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 15:02:10 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:06:48 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:03:00 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:15 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:07:47 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:06:13 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:09:33 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:02:28 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:01:33 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:07:49 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:06:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-10 15:05:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:03:30 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:02:57 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:02:41 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:01:25 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:02:13 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-05-10 15:04:04 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-05-10 15:07:46 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.019 |  |
| 2026-05-10 15:06:19 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-10 15:01:57 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-05-10 15:06:59 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-05-10 15:03:00 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.023 |  |
| 2026-05-10 15:09:25 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.028 |  |
| 2026-05-10 15:08:26 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.028 |  |
| 2026-05-10 15:09:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.037 |  |
| 2026-05-10 15:02:31 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-05-10 15:04:36 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.040 |  |
| 2026-05-10 15:02:24 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.050 |  |
| 2026-05-10 15:07:19 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | -0.064 |  |
| 2026-05-10 14:02:19 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)