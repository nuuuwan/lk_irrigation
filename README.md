# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_18:15:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,136 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 18:15:41 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:12:18 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:10:00 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.028 |  |
| 2026-06-16 18:09:26 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-06-16 18:08:55 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:08:17 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-16 18:07:22 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:06:55 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.060 |  |
| 2026-06-16 18:06:32 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-16 18:06:25 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:06:01 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:05:55 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:04:59 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:04:51 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.022 |  |
| 2026-06-16 18:04:09 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:04:06 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.063 |  |
| 2026-06-16 18:04:04 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:04:02 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.121 |  |
| 2026-06-16 18:03:58 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:03:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-16 18:03:21 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.022 |  |
| 2026-06-16 18:03:07 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 18:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.011 |  |
| 2026-06-16 18:02:49 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:37 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-16 18:02:30 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:13 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-06-16 18:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:08 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:00 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:01:49 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:01:43 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:01:28 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-06-16 18:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:01:11 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:01:09 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-16 18:00:54 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:21 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 18:08:17 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-16 18:06:32 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-16 18:01:09 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-16 18:03:07 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 18:02:37 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-16 18:04:04 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:01:43 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:03:58 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:01:11 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:05:55 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:07:22 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:04:59 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:01:49 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:04:09 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:03:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:15:41 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:06:01 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:30 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:12:18 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:08 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:09:26 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-06-16 18:02:00 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:06:25 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:00:54 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-16 18:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.63 | 🟢 Normal | -0.011 |  |
| 2026-06-16 18:02:49 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-16 18:01:28 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-06-16 18:04:51 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.022 |  |
| 2026-06-16 18:03:21 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.022 |  |
| 2026-06-16 18:10:00 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.028 |  |
| 2026-06-16 18:02:13 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-16 18:06:55 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.060 |  |
| 2026-06-16 18:04:06 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.063 |  |
| 2026-06-16 18:04:02 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)