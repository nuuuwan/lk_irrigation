# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_07:00:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,060 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 07:00:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.022 |  |
| 2026-01-05 07:00:50 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.002 |  |
| 2026-01-05 07:00:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:19 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:15 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 06:35:53 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-01-05 06:18:15 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:14:50 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-05 06:12:48 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:10:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:09:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:09:06 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:08:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:07:55 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:07:37 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:06:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.022 |  |
| 2026-01-05 06:06:41 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:06:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.206 |  |
| 2026-01-05 06:06:33 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-01-05 06:06:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-05 06:05:52 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:05:39 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:05:33 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:05:03 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-05 06:05:00 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:04:51 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 06:04:35 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:04:19 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:04:17 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:04:16 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-05 06:04:01 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.024 |  |
| 2026-01-05 06:03:31 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-05 06:03:26 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 06:03:03 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 06:14:50 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-05 06:02:31 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 06:06:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-05 06:05:03 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-05 06:03:03 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 06:03:26 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 07:00:15 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 06:04:51 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 06:02:42 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-05 06:10:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:02:12 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:05:33 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:07:55 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:02:26 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:12:48 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:02:54 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:05:52 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:19 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:05:00 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:04:35 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:04:19 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:05:39 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:18:15 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:06:41 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:01:56 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-05 06:09:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:50 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.002 |  |
| 2026-01-05 06:04:16 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-05 06:03:31 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-05 06:01:24 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-01-05 07:00:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.022 |  |
| 2026-01-05 06:04:01 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.024 |  |
| 2026-01-05 06:06:33 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.028 |  |
| 2026-01-05 06:02:26 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.041 |  |
| 2026-01-05 06:01:48 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.080 |  |
| 2026-01-05 06:35:53 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-01-05 06:01:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.155 |  |
| 2026-01-05 06:06:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)