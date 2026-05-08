# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_22:31:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 22:31:47 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 22:17:08 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 22:12:32 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 22:07:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-05-08 22:07:51 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-05-08 22:07:08 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-05-08 22:07:07 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-08 22:06:17 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | 0.885 | 🔺 Rising |
| 2026-05-08 22:06:06 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.212 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 22:02:06 | Thanamalwila (Kirindi Oya) | 5.29 | 🟠 Minor Flood | 1.308 | 🔺 Rising |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-08 22:06:17 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | 0.885 | 🔺 Rising |
| 2026-05-08 22:00:23 | Kuda Oya (Kirindi Oya) | 6.70 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-05-08 22:07:51 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-05-08 22:06:06 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-08 21:01:50 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-08 22:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-08 22:01:17 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-08 22:12:32 | Thaldena (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 22:05:11 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 22:02:09 | Moragaswewa (Deduru Oya) | 1.83 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-08 22:07:07 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-08 22:31:47 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 22:17:08 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 22:02:01 | Moraketiya (Walawe Ganga) | 1.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 22:03:14 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-08 22:01:44 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 22:02:09 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 22:01:52 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-08 22:00:40 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 22:03:56 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-08 22:01:08 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-08 22:04:03 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-08 22:07:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-05-08 22:05:23 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-05-08 22:01:54 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-08 22:03:11 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-05-08 22:04:51 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-05-08 22:01:17 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.020 |  |
| 2026-05-08 22:05:16 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.027 |  |
| 2026-05-08 22:07:08 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-08 22:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-05-08 22:05:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-05-08 22:03:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-05-08 22:03:46 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.120 |  |
| 2026-05-08 22:00:49 | Wellawaya (Kirindi Oya) | 3.24 | 🟢 Normal | -0.392 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)