# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_08:08:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 08:08:16 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 08:07:29 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 08:06:51 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:06:43 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-11 08:06:10 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-11 08:05:41 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.028 |  |
| 2026-06-11 08:05:25 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:05:16 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:05:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:05:04 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 08:04:51 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 08:04:30 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 08:03:39 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 08:03:28 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:03:05 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-11 08:02:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-11 08:02:50 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:02:49 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-06-11 08:02:48 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:02:07 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:44 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:31 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:28 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:16 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-06-11 08:01:12 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-06-11 08:01:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:09 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-06-11 08:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:00:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-11 08:00:31 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:00:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:00:24 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:22:46 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:18:26 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 07:06:33 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-06-11 08:00:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-11 08:03:05 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-11 08:06:10 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-11 08:06:43 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-11 08:08:16 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 08:07:29 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-11 08:05:04 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-11 07:00:53 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 08:04:51 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 08:04:30 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 07:17:02 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-11 08:03:39 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 08:02:07 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:00:31 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:31 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:03:28 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:05:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:08:59 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:10:56 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:05:25 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:05:16 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:02:48 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:02:50 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:44 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:06:51 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-11 07:05:05 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:00:24 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:00:31 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:01:28 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2026-06-11 08:02:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-11 08:02:49 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-06-11 08:01:09 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-06-11 08:01:12 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-06-11 08:05:41 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.028 |  |
| 2026-06-11 08:01:16 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)