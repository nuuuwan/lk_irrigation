# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_12:08:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,776 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 12:08:27 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-05-12 12:07:48 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:07:38 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.033 |  |
| 2026-05-12 12:07:21 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:07:09 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-05-12 12:06:53 | Katharagama (Menik Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-05-12 12:06:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | -0.021 |  |
| 2026-05-12 12:06:05 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-12 12:05:58 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-12 12:05:40 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-05-12 12:05:32 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 12:05:32 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:05:31 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-12 12:04:32 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:04:15 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-05-12 12:03:33 | Thanthirimale (Malwathu Oya) | 3.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 12:03:24 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 12:03:21 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:03:12 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.079 |  |
| 2026-05-12 12:03:10 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.060 |  |
| 2026-05-12 12:03:06 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-05-12 12:03:03 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:02:59 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.041 |  |
| 2026-05-12 12:02:39 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:02:38 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:02:36 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 12:02:35 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-05-12 12:02:33 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-12 12:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.042 |  |
| 2026-05-12 12:02:23 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:02:17 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-12 12:01:56 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:01:45 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:01:43 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:01:33 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:01:31 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.169 |  |
| 2026-05-12 12:01:13 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.030 |  |
| 2026-05-12 12:00:26 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:00:08 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.046 |  |
| 2026-05-12 11:59:08 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-05-12 11:31:13 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 11:59:08 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-05-12 12:02:17 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-12 12:06:05 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-12 12:05:31 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-12 12:02:33 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-12 12:05:58 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-12 12:03:24 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 12:02:36 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 12:03:33 | Thanthirimale (Malwathu Oya) | 3.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 11:03:39 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 12:05:32 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 12:07:48 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:02:39 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:03:21 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:04:32 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:02:23 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:03:03 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:07:21 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:01:43 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:01:56 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:00:26 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:01:33 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:05:32 | Moragaswewa (Deduru Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-05-12 12:06:53 | Katharagama (Menik Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-05-12 12:08:27 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-05-12 12:03:06 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-05-12 12:06:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | -0.021 |  |
| 2026-05-12 12:05:40 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-05-12 12:07:09 | Thanamalwila (Kirindi Oya) | 2.02 | 🟢 Normal | -0.030 |  |
| 2026-05-12 12:02:35 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-05-12 12:01:13 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.030 |  |
| 2026-05-12 12:07:38 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.033 |  |
| 2026-05-12 12:04:15 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-05-12 12:02:59 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.041 |  |
| 2026-05-12 12:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.042 |  |
| 2026-05-12 12:00:08 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.046 |  |
| 2026-05-12 12:03:10 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.060 |  |
| 2026-05-12 12:03:12 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.079 |  |
| 2026-05-12 12:01:31 | Weraganthota (Mahaweli Ganga) | -2.44 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)