# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_09:27:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,272 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 09:27:41 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.007 |  |
| 2026-05-16 09:22:55 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-05-16 09:08:30 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:07:23 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:06:55 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.041 |  |
| 2026-05-16 09:06:26 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:06:07 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.190 |  |
| 2026-05-16 09:05:58 | Galgamuwa (Mee Oya) | 3.63 | 🟢 Normal | -0.020 |  |
| 2026-05-16 09:05:55 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:05:53 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | -0.055 |  |
| 2026-05-16 09:05:38 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.082 |  |
| 2026-05-16 09:05:22 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-05-16 09:05:13 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-05-16 09:05:02 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | -0.032 |  |
| 2026-05-16 09:04:41 | Dunamale (Aththanagalu Oya) | 4.34 | 🟡 Alert | -0.039 |  |
| 2026-05-16 09:04:40 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:04:31 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:04:22 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.040 |  |
| 2026-05-16 09:04:12 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-05-16 09:04:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:04:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:03:43 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.082 |  |
| 2026-05-16 09:03:34 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | -0.532 |  |
| 2026-05-16 09:03:12 | Magura (Kalu Ganga) | 3.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-16 09:03:00 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 09:02:33 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.071 |  |
| 2026-05-16 09:02:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:02:22 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.050 |  |
| 2026-05-16 09:02:06 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-05-16 09:01:53 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.266 |  |
| 2026-05-16 09:01:53 | Ellagawa (Kalu Ganga) | 8.47 | 🟢 Normal | -0.030 |  |
| 2026-05-16 09:01:49 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:01:42 | Thanthirimale (Malwathu Oya) | 4.05 | 🟢 Normal | -0.030 |  |
| 2026-05-16 09:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:01:31 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-05-16 09:01:10 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:00:53 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 09:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.04 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 09:04:41 | Dunamale (Aththanagalu Oya) | 4.34 | 🟡 Alert | -0.039 |  |
| 2026-05-16 09:03:12 | Magura (Kalu Ganga) | 3.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-16 09:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:01:31 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:01:10 | Moragaswewa (Deduru Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:08:30 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:07:23 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:05:55 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:04:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:04:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:02:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:04:40 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:00:53 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-16 09:27:41 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.007 |  |
| 2026-05-16 09:22:55 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-05-16 09:05:22 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-05-16 09:01:49 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:03:00 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:04:31 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:06:26 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-16 09:05:13 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-05-16 09:02:06 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-05-16 09:04:12 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-05-16 09:05:58 | Galgamuwa (Mee Oya) | 3.63 | 🟢 Normal | -0.020 |  |
| 2026-05-16 09:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-05-16 09:01:53 | Ellagawa (Kalu Ganga) | 8.47 | 🟢 Normal | -0.030 |  |
| 2026-05-16 09:01:42 | Thanthirimale (Malwathu Oya) | 4.05 | 🟢 Normal | -0.030 |  |
| 2026-05-16 09:05:02 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | -0.032 |  |
| 2026-05-16 09:04:22 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.040 |  |
| 2026-05-16 09:06:55 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.041 |  |
| 2026-05-16 09:02:22 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.050 |  |
| 2026-05-16 09:05:53 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | -0.055 |  |
| 2026-05-16 09:02:33 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.071 |  |
| 2026-05-16 09:05:38 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.082 |  |
| 2026-05-16 09:03:43 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.082 |  |
| 2026-05-16 09:06:07 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.190 |  |
| 2026-05-16 09:01:53 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.266 |  |
| 2026-05-16 09:03:34 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | -0.532 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)