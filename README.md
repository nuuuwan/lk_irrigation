# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_08:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 08:15:08 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-02-10 08:13:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.053 |  |
| 2026-02-10 08:09:57 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:09:17 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-02-10 08:09:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:08:12 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:07:49 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.075 |  |
| 2026-02-10 08:07:00 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:06:28 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:06:15 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:05:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:05:52 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-10 08:05:40 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:05:33 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:05:10 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-02-10 08:04:15 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:02 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:01 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:03:46 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-10 08:03:16 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:03:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:03:06 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:03:04 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-02-10 08:02:58 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:47 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:02:29 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.020 |  |
| 2026-02-10 08:02:29 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:25 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:13 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:13 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.043 |  |
| 2026-02-10 08:02:05 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:01:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:01:50 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.050 |  |
| 2026-02-10 08:01:38 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:00:56 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:00:31 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 07:49:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.216 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 08:09:17 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-02-10 06:01:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-10 08:03:46 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-10 08:00:31 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-10 08:05:52 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-10 08:03:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:02 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:29 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:06:28 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:01:38 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:15 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:08:12 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:58 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:07:00 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:06:15 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 07:02:11 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:13 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:09:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:05:33 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:01 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:04:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:03:16 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:05:40 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:05:10 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:09:57 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:03:06 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:02:25 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 08:05:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:02:47 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:02:05 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:00:56 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-10 08:02:29 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.020 |  |
| 2026-02-10 08:15:08 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-02-10 08:03:04 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-02-10 08:04:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-02-10 08:02:13 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.043 |  |
| 2026-02-10 08:01:50 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.050 |  |
| 2026-02-10 08:13:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.053 |  |
| 2026-02-10 08:07:49 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)