# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_09:35:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,895 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 09:35:49 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:13:41 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-07-04 09:10:53 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:09:25 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-07-04 09:09:17 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:09:15 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:08:40 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-07-04 09:08:25 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:08:12 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-04 09:07:58 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:07:19 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:06:59 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:06:09 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:05:54 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-04 09:05:12 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:04:42 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 09:04:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:04:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-07-04 09:04:16 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 09:04:15 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-04 09:04:14 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:04:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.019 |  |
| 2026-07-04 09:03:57 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 09:03:36 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-04 09:03:08 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:56 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:54 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 09:02:54 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.087 |  |
| 2026-07-04 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.059 |  |
| 2026-07-04 09:02:42 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:39 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-04 09:02:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:12 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.067 |  |
| 2026-07-04 09:02:11 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:08 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 09:02:04 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:02 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 09:01:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-07-04 09:01:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:01:22 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-04 09:00:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 09:08:40 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-07-04 09:13:41 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-07-04 09:09:25 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-07-04 09:01:22 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-04 09:05:54 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-04 09:03:36 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-04 09:02:39 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-04 09:08:12 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-04 09:04:15 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-04 09:02:02 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 09:02:08 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-04 09:03:57 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 09:02:54 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 09:00:11 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 09:04:16 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 09:04:42 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 09:00:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:06:59 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:01:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:08:25 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:07:19 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:04:14 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:03:08 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:04:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:11 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:56 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:42 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:35:49 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:10:53 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:02:04 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:09:17 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:05:12 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 09:04:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-07-04 09:04:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.019 |  |
| 2026-07-04 09:01:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-07-04 09:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.059 |  |
| 2026-07-04 09:02:12 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.067 |  |
| 2026-07-04 09:02:54 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)